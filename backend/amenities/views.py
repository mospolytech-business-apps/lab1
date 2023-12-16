from rest_framework import viewsets

from amenities.models import Amenity, AmenityCabinType, AmenityTicket
from amenities.serializers import (
    AmenitySerializer,
    AmenityCabinTypeSerializer,
    AmenityTicketSerializer,
)
from rest_framework.decorators import action
from rest_framework.response import Response
from tickets.models import Ticket
from cabintypes.models import CabinType
from schedules.models import Schedule
from office.models import Office
from django.db.models import Count
from authentication.models import User
from datetime import datetime, timedelta
from django.db import IntegrityError
from datetime import date
import time
import math


class AmenityViewSet(viewsets.ModelViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer

    @action(detail=False, methods=["post"], url_path="search")
    def amenities_report(self, request):
        booking_reference = request.data.get("booking_reference")

        if not booking_reference:
            return Response(
                {"error": "Необходимо указать код бронирования."},
                status=400,
            )

        try:
            ticket = Ticket.objects.get(booking_reference=booking_reference)

            today = datetime.now()
            today = datetime(2017, 10, 9, 12, 0, 0)

            # Check if the flight has already left
            flight_datetime = datetime.combine(
                ticket.schedule.Date, ticket.schedule.Time
            )
            if flight_datetime < today:
                return Response(
                    {"error": "Сервис недоступен, так как рейс уже состоялся."},
                    status=400,
                )

            passenger_data = {
                "name": f"{ticket.first_name} {ticket.last_name}",
                "passport": ticket.passport_number,
                "cabin_type": ticket.cabin_type.name,
            }

            result_data = {
                "ticket": {
                    "id": ticket.id,
                    "schedule": {
                        "id": ticket.schedule.id,
                        "departure_airport": ticket.schedule.Route.DepartureAirport.IATACode,
                        "arrival_airport": ticket.schedule.Route.ArrivalAirport.IATACode,
                        "date": str(ticket.schedule.Date),
                        "time": str(ticket.schedule.Time),
                    },
                },
                "amenities": [],
            }

            default_list = []
            if ticket.cabin_type.name == "Economy":
                default_list = [
                    "Wi-Fi 50 mb",
                    "Soft Drinks",
                ]
            elif ticket.cabin_type.name == "Business":
                default_list = [
                    "Wi-Fi 50 mb",
                    "Wi-Fi 250 mb",
                    "Fast Checkin Lane",
                    "Soft Drinks",
                    "Laptop Rental",
                    "Tablet Rental",
                ]
            elif ticket.cabin_type.name == "First Class":
                default_list = [
                    "Wi-Fi 50 mb",
                    "Wi-Fi 250 mb",
                    "Fast Checkin Lane",
                    "Extra Bag",
                    "Premium Headphones Rental",
                    "Soft Drinks",
                    "Lounge Access",
                    "Laptop Rental",
                    "Tablet Rental",
                    "Extra Blanket",
                ]

            amenities_data = AmenityTicket.objects.filter(ticket=ticket)
            ticket_amenities_names = [t.amenity.name for t in amenities_data]

            all_amenities = Amenity.objects.values("name", "price")
            for amenity in all_amenities:
                result_data["amenities"].append(
                    {
                        "name": amenity["name"],
                        "price": amenity["price"],
                        "default": amenity["name"] in default_list,
                        "selected": amenity["name"] in ticket_amenities_names,
                    }
                )

            response_data = {
                "passenger": passenger_data,
                "data": [result_data],
            }

            return Response(response_data)

        except Ticket.DoesNotExist:
            return Response(
                {"error": "Билет с указанным кодом бронирования не найден."}, status=404
            )
        except Exception as e:
            return Response({"error": f"Произошла ошибка: {str(e)}"}, status=500)

    @action(detail=False, methods=["get"], url_path="short-summary")
    def short_summary(self, request):
        today = date(2017, 12, 28)
        thirty_days_ago = today - timedelta(days=30)

        start_time = time.time()

        # Flights stats
        confirmed_tickets = Ticket.objects.filter(
            schedule__Date__gte=thirty_days_ago, confirmed=True
        )
        canceled_tickets = Ticket.objects.filter(
            schedule__Date__gte=thirty_days_ago, confirmed=False
        )

        confirmed_flights_count = confirmed_tickets.count()
        canceled_flights_count = canceled_tickets.count()

        # Average flight time
        schedules = Schedule.objects.filter(Date__range=[thirty_days_ago, today])
        number_of_flights = Schedule.objects.filter(
            Date__range=[thirty_days_ago, today]
        ).count()

        total_duration = 0
        for schedule in schedules:
            flight_time = schedule.Route.FlightTime
            total_duration += flight_time

        average_daily_flight_time = int(total_duration / number_of_flights)

        # Busiest and quietest days in last 30 days
        schedules = Schedule.objects.filter(Date__range=[thirty_days_ago, today])
        date_counts = schedules.values("Date").annotate(count=Count("id"))

        max_date = max(date_counts, key=lambda x: x["count"])
        max_schedules = max_date["count"]

        min_date = min(date_counts, key=lambda x: x["count"])
        min_schedules = min_date["count"]

        # Top clients in last 30 days
        top_clients = (
            Ticket.objects.filter(schedule__Date__range=[thirty_days_ago, today])
            .values("user__first_name", "user__last_name")
            .annotate(count=Count("passport_number", distinct=True))
            .order_by("-count")[:5]
        )

        # Top offices
        top_offices = (
            Ticket.objects.filter(schedule__Date__range=[thirty_days_ago, today])
            .values("user__office__title")
            .annotate(count=Count("id"))
            .order_by("-count")[:5]
        )

        # Revenue from tickets sales (yesterday, 2 days ago, 3 days ago)
        revenues = []
        for d in [
            today - timedelta(days=1),
            today - timedelta(days=2),
            today - timedelta(days=3),
        ]:
            tickets = Ticket.objects.filter(
                schedule__Date__range=[d, today], confirmed=True
            )
            rev = 0
            for ticket in tickets:
                price_multiplier = 1
                if ticket.cabin_type == "First Class":
                    price_multiplier = 1.30 * 1.35
                elif ticket.cabin_type == "Business":
                    price_multiplier = 1.30

                rev += ticket.schedule.EconomyPrice * price_multiplier

            revenues.append({"date": str(d), "amount": int(rev)})

        yesterday_revenue = revenues[0]["amount"]
        two_days_ago_revenue = revenues[1]["amount"]
        three_days_ago_revenue = revenues[2]["amount"]

        # Weakly report of percentage of empty seats (this week, last week, 2 weeks ago)
        # this week
        last_week = today - timedelta(weeks=1)
        tickets_this_week = Ticket.objects.filter(
            schedule__Date__range=[last_week, today]
        )
        schedules_this_week = Schedule.objects.filter(Date__range=[last_week, today])
        seats_this_week = sum(s.Aircraft.TotalSeats for s in schedules_this_week)
        empty_pct_this_week = (
            100 * (seats_this_week - tickets_this_week.count()) / seats_this_week
        )

        # last week
        last_week = today - timedelta(weeks=2)
        tickets_last_week = Ticket.objects.filter(
            schedule__Date__range=[last_week, today]
        )
        schedules_last_week = Schedule.objects.filter(Date__range=[last_week, today])
        seats_last_week = sum(s.Aircraft.TotalSeats for s in schedules_last_week)
        empty_pct_last_week = (
            100 * (seats_last_week - tickets_last_week.count()) / seats_last_week
        )

        # two weeks ago
        two_weeks_ago = today - timedelta(weeks=3)
        tickets_two_weeks_ago = Ticket.objects.filter(
            schedule__Date__range=[two_weeks_ago, today]
        )
        schedules_two_weeks_ago = Schedule.objects.filter(
            Date__range=[two_weeks_ago, today]
        )
        seats_two_weeks_ago = sum(
            s.Aircraft.TotalSeats for s in schedules_two_weeks_ago
        )
        empty_pct_two_weeks_ago = (
            100
            * (seats_two_weeks_ago - tickets_two_weeks_ago.count())
            / seats_two_weeks_ago
        )

        def truncate(f, n):
            return math.floor(f * 10**n) / 10**n

        response = {
            "flights": {
                "confirmed": confirmed_flights_count,
                "cancelled": canceled_flights_count,
                "average_daily_flight_time": average_daily_flight_time,
            },
            "number_of_passengers": {
                "busiest": {"day": max_date["Date"], "flights": max_schedules},
                "quietest": {"day": min_date["Date"], "flights": min_schedules},
            },
            "top_clients": [
                {
                    "name": f"{client['user__first_name']} {client['user__last_name']}",
                    "flights": client["count"],
                }
                for client in top_clients
            ],
            "top_offices": [
                {"name": office["user__office__title"], "flights": office["count"]}
                for office in top_offices
            ],
            "revenue": {
                "yesterday": yesterday_revenue,
                "two_days_ago": two_days_ago_revenue,
                "three_days_ago": three_days_ago_revenue,
            },
            "weekly_seats_empty": {
                "this_week": truncate(empty_pct_this_week, 2),
                "last_week": truncate(empty_pct_last_week, 2),
                "two_weeks_ago": truncate(empty_pct_two_weeks_ago, 2),
            },
        }

        end_time = time.time()
        response["report_generated_in"] = truncate(end_time - start_time, 3)

        return Response(response)

    @action(
        detail=False,
        methods=["POST"],
        url_path="purchase-amenities-for-ticket/(?P<id>\d+)",
    )
    def purchase_amenities(self, request, id):
        # Get ticket
        try:
            ticket = Ticket.objects.get(id=id)
        except Ticket.DoesNotExist:
            return Response({"error": "Invalid ticket id"}, status=400)

        # Get amenities to add
        amenities_ids = request.data.get("amenities_id")
        if not amenities_ids:
            return Response({"error": "No amenities specified"})

        try:
            amenities = Amenity.objects.filter(id__in=amenities_ids)
        except Amenity.DoesNotExist:
            return Response({"error": "Invalid amenity id"})

        # Add each amenity to ticket, checking for existence first
        for amenity in amenities:
            # Check if the pair already exists
            if AmenityTicket.objects.filter(ticket=ticket, amenity=amenity).exists():
                return Response(
                    {"error": "Amenity already purchased for this ticket"}, status=400
                )

            # Create the AmenityTicket entry
            try:
                AmenityTicket.objects.create(ticket=ticket, amenity=amenity)
            except IntegrityError:
                return Response({"error": "Failed to purchase amenity"}, status=500)

        return Response({"message": "Amenities purchased successfully"})

    @action(detail=False, methods=["POST"], url_path="amenities-report")
    def amenities_report(self, request):
        flight_id = request.data.get("flight_id")
        start_date = request.data.get("start_date")
        end_date = request.data.get("end_date")

        if flight_id and not (start_date) and not (end_date):
            amenity_tickets = AmenityTicket.objects.filter(
                ticket__schedule__FlightNumber=flight_id
            )
        elif not (flight_id) and start_date and end_date:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
            amenity_tickets = AmenityTicket.objects.filter(
                ticket__schedule__Date__range=[start_date, end_date]
            )
            print(amenity_tickets)

        amenity_names = []
        amenity_data = {
            "Economy": [],
            "Business": [],
            "First Class": [],
        }

        for at in amenity_tickets:
            amenity = at.amenity
            cabin_class = at.ticket.cabin_type.name

            print(amenity.name, cabin_class)

            if amenity.name not in amenity_names:
                amenity_names.append(amenity.name)
                amenity_data["Economy"].append(0)
                amenity_data["Business"].append(0)
                amenity_data["First Class"].append(0)

            amenity_index = amenity_names.index(amenity.name)
            amenity_data[cabin_class][amenity_index] += 1

        # Format response
        response_data = {
            "economy": amenity_data["Economy"],
            "business": amenity_data["Business"],
            "first": amenity_data["First Class"],
        }

        return Response({"amenities": amenity_names, "data": response_data})
