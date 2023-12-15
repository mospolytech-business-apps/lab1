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
from datetime import date
import time
import math


class AmenityViewSet(viewsets.ModelViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer

    @action(detail=False, methods=["post"], url_path="amenities-report")
    def amenities_report(self, request):
        booking_reference = request.data.get("booking_reference")
        start_time = request.data.get("start_time")
        end_time = request.data.get("end_time")

        if not booking_reference and not (start_time or end_time):
            return Response(
                {
                    "error": "Необходимо указать либо код бронирования, либо идентификатор рейса, начальное и конечное время."
                },
                status=400,
            )

        try:
            if booking_reference:
                ticket = Ticket.objects.get(booking_reference=booking_reference)
                amenities_data = AmenityTicket.objects.filter(ticket=ticket).values(
                    "amenity__name",
                    "ticket__cabin_type",
                    "ticket__first_name",
                    "ticket__last_name",
                    "ticket__passport_number",
                )
                return Response(
                    {"class": ticket.cabin_type.name, "data": list(amenities_data)}
                )

            elif start_time or end_time:
                tickets = Ticket.objects.filter(
                    schedule__Date__gte=start_time, schedule__Date__lte=end_time
                )

                if not tickets.exists():
                    return Response({"error": "Билеты не найдены."}, status=404)

                # Сбор всех подходящих под фильтр объектов AmenityTicket
                amenities_data = AmenityTicket.objects.filter(
                    ticket__in=tickets
                ).values(
                    "amenity__name",
                    "ticket__cabin_type",
                    "ticket__first_name",
                    "ticket__last_name",
                    "ticket__passport_number",
                )

                if not amenities_data.exists():
                    return Response(
                        {"error": "Данные по услугам не найдены."}, status=404
                    )

                # Форматирование данных как указано
                amenities = [item["amenity__name"] for item in amenities_data]
                statistics = {}
                for item in amenities_data:
                    if item["ticket__cabin_type"] not in statistics:
                        statistics[item["ticket__cabin_type"]] = [0, 0, 0, 0]

                    # Пример подсчета количества услуг для каждого класса
                    if item["amenity__name"] == "Some Amenity":
                        statistics[item["ticket__cabin_type"]][0] += 1
                    elif item["amenity__name"] == "Another Amenity":
                        statistics[item["ticket__cabin_type"]][1] += 1

                result = {
                    "amenities": amenities,
                    "statistics": [
                        {"class": key, "data": value}
                        for key, value in statistics.items()
                    ],
                }

                return Response(result)

        except (Ticket.DoesNotExist, Schedule.DoesNotExist):
            return Response({"error": "Билет или рейс не найден."}, status=404)
        except Exception as e:
            return Response({"error": f"Произошла ошибка: {str(e)}"}, status=500)

    @action(detail=False, methods=["get"], url_path="full-report")
    def full_report(self, request):
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

        # two weeks ago
        two_weeks_ago = today - timedelta(weeks=2)
        tickets_last_week = Ticket.objects.filter(
            schedule__Date__range=[two_weeks_ago, today]
        )
        schedules_last_week = Schedule.objects.filter(
            Date__range=[two_weeks_ago, today]
        )
        seats_last_week = sum(s.Aircraft.TotalSeats for s in schedules_last_week)
        empty_pct_last_week = (
            100 * (seats_last_week - tickets_last_week.count()) / seats_last_week
        )

        # three weeks ago
        three_weeks_ago = today - timedelta(weeks=3)
        tickets_two_weeks_ago = Ticket.objects.filter(
            schedule__Date__range=[three_weeks_ago, today]
        )
        schedules_two_weeks_ago = Schedule.objects.filter(
            Date__range=[three_weeks_ago, today]
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
                "yesterday": truncate(empty_pct_this_week, 2),
                "two_days_ago": truncate(empty_pct_last_week, 2),
                "three_days_ago": truncate(empty_pct_two_weeks_ago, 2),
            },
        }

        end_time = time.time()
        response["report_generated_in"] = truncate(end_time - start_time, 3)

        return Response(response)

    @action(detail=False, url_path="amenities-tickets")
    def amenities_tickets(self, request):
        items = AmenityTicket.objects.all()
        serializer = AmenityTicketSerializer(items, many=True)
        return Response(serializer.data)
