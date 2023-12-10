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

        # Общий результат
        result = {
            "amenities": {"amenities": list(amenities_data)},
            "top_clients": {"top_clients": list(top_clients)},
            "top_offices": {"top_offices": list(top_offices)},
            "flight_counts": {
                "confirmed_flights_count": confirmed_flights_count,
                "canceled_flights_count": canceled_flights_count,
            },
            "average_flight_duration": str(average_duration),
        }

        return Response(result)

    @action(detail=False, url_path="amenities-tickets")
    def amenities_tickets(self, request):
        items = AmenityTicket.objects.all()
        serializer = AmenityTicketSerializer(items, many=True)
        return Response(serializer.data)
