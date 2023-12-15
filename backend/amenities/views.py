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

class AmenityViewSet(viewsets.ModelViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer

    @action(detail=False, methods=["post"], url_path="amenities-report")
    def amenities_report(self, request):
        booking_reference = request.data.get("booking_reference")

        if not booking_reference:
            return Response(
                {"error": "Необходимо указать код бронирования."},
                status=400,
            )

        try:
            ticket = Ticket.objects.get(booking_reference=booking_reference)

            amenities_data = AmenityTicket.objects.filter(ticket=ticket).values(
                "amenity__name",
                "amenity__price",
                "ticket__id",
                "ticket__schedule__id",
                "ticket__schedule__Route__DepartureAirport__IATACode",  # Изменение здесь
                "ticket__schedule__Route__ArrivalAirport__IATACode",    # Изменение здесь
                "ticket__schedule__Date",
                "ticket__schedule__Time",
            )

            passenger_data = {
                "name": f"{ticket.first_name} {ticket.last_name}",
                "passport": ticket.passport_number,
                "cabin_type": ticket.cabin_type.name,
            }

            result_data = []
            for item in amenities_data:
                result_data.append({
                    "ticket": {
                        "id": item["ticket__id"],
                        "schedule": {
                            "id": item["ticket__schedule__id"],
                            "departure_airport": item["ticket__schedule__Route__DepartureAirport__IATACode"],  # Изменение здесь
                            "arrival_airport": item["ticket__schedule__Route__ArrivalAirport__IATACode"],  # Изменение здесь
                            "date": str(item["ticket__schedule__Date"]),
                            "time": str(item["ticket__schedule__Time"]),
                        },
                    },
                    "amenities": [
                        {
                            "name": item["amenity__name"],
                            "price": item["amenity__price"],
                            "default": True,  # Может потребоваться настроить в соответствии с вашей логикой
                            "selected": True,
                        }
                    ]
                })

            response_data = {
                "passenger": passenger_data,
                "data": result_data,
            }

            return Response(response_data)

        except Ticket.DoesNotExist:
            return Response({"error": "Билет с указанным кодом бронирования не найден."}, status=404)
        except Exception as e:
            return Response({"error": f"Произошла ошибка: {str(e)}"}, status=500)

    @action(detail=False, methods=["get"], url_path="full-report")
    def full_report(self, request):
        # Получение данных по Amenity
        amenities = Amenity.objects.all()
        amenities_data = AmenityTicket.objects.filter(amenity__in=amenities).values(
            "amenity__name",
            "ticket__cabin_type",
            "ticket__first_name",
            "ticket__last_name",
            "ticket__passport_number",
        )

        # Получение топ клиентов
        top_clients = (
            Ticket.objects.values("user__email")
            .annotate(total_tickets=Count("id"))
            .order_by("-total_tickets")[:5]
        )

        # Получение топ офисов
        top_offices = (
            Office.objects.values("title")
            .annotate(total_tickets=Count("user__id"))
            .order_by("-total_tickets")[:5]
        )

        # Получение количества confirmed и canceled рейсов
        flight_status_counts = (
            Ticket.objects.values("confirmed")
            .annotate(count=Count("id"))
            .order_by("-count")
        )

        confirmed_flights_count = 0
        canceled_flights_count = 0
        for status_count in flight_status_counts:
            if status_count["confirmed"]:
                confirmed_flights_count = status_count["count"]
            else:
                canceled_flights_count = status_count["count"]

        # Calculate average flight duration
        confirmed_tickets = Ticket.objects.filter(confirmed=True)
        total_duration = timedelta()
        for ticket in confirmed_tickets:
            flight_start_time = datetime.combine(ticket.schedule.Date, ticket.schedule.Time)
            flight_end_time = flight_start_time + timedelta(minutes=ticket.schedule.Route.FlightTime)
            duration = flight_end_time - flight_start_time
            total_duration += duration

        average_duration = total_duration / len(confirmed_tickets)

        # Calculate busiest and least busy days
        flight_counts_by_day = Schedule.objects.filter(
            Date__in=confirmed_tickets.values("schedule__Date")
        ).values("Date").annotate(total_flights=Count("id")).order_by("-total_flights")

        busiest_day = flight_counts_by_day.first()
        least_busy_day = flight_counts_by_day.last()

        # Общий результат
        result = {
            "amenities": {"amenities": list(amenities_data)},
            "top_clients": {"top_clients": list(top_clients)},
            "top_offices": {"top_offices": list(top_offices)},
            "flight_counts": {
                "confirmed_flights_count": confirmed_flights_count,
                "canceled_flights_count": canceled_flights_count,
                "average_flight_duration": str(average_duration),
                "busiest_day": busiest_day["Date"] if busiest_day else None,
                "least_busy_day": least_busy_day["Date"] if least_busy_day else None,
            },
        }

        return Response(result)

    @action(detail=False, url_path="amenities-tickets")
    def amenities_tickets(self, request):
        items = AmenityTicket.objects.all()
        serializer = AmenityTicketSerializer(items, many=True)
        return Response(serializer.data)
