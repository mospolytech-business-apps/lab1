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


class AmenityViewSet(viewsets.ModelViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer

    @action(detail=False, methods=['post'], url_path="amenities-report")
    def amenities_report(self, request):
        booking_reference = request.data.get('booking_reference')
        flight_id = request.data.get('flight_id')
        start_time = request.data.get('start_time')
        end_time = request.data.get('end_time')

        if not booking_reference and not (flight_id and start_time and end_time):
            return Response({"error": "Необходимо указать либо код бронирования, либо идентификатор рейса, начальное и конечное время."}, status=400)

        try:
            if booking_reference:
                ticket = Ticket.objects.get(booking_reference=booking_reference)
                amenities_data = AmenityTicket.objects.filter(ticket=ticket).values(
                    'amenity__name', 'ticket__cabin_type', 'ticket__first_name', 'ticket__last_name', 'ticket__passport_number'
                )
                return Response({"class": ticket.cabin_type.name, "data": list(amenities_data)})
            
            elif flight_id and start_time and end_time:
                schedule = Schedule.objects.get(pk=flight_id)
                tickets = Ticket.objects.filter(schedule=schedule, schedule__Date__gte=start_time, schedule__Date__lte=end_time)

                amenities_data = AmenityTicket.objects.filter(ticket__in=tickets).values(
                    'amenity__name', 'ticket__cabin_type', 'ticket__first_name', 'ticket__last_name', 'ticket__passport_number'
                )

                # Форматирование данных как указано
                amenities = [item['amenity__name'] for item in amenities_data]
                statistics = {}
                for item in amenities_data:
                    if item['ticket__cabin_type'] not in statistics:
                        statistics[item['ticket__cabin_type']] = [0, 0, 0, 0]

                    # Пример подсчета количества услуг для каждого класса
                    if item['amenity__name'] == "Some Amenity":
                        statistics[item['ticket__cabin_type']][0] += 1
                    elif item['amenity__name'] == "Another Amenity":
                        statistics[item['ticket__cabin_type']][1] += 1


                result = {
                    "amenities": amenities,
                    "statistics": [
                        {"class": key, "data": value} for key, value in statistics.items()
                    ]
                }

                return Response(result)

        except (Ticket.DoesNotExist, Schedule.DoesNotExist):
            return Response({"error": "Билет или рейс не найден."}, status=404)
        except Exception as e:
            return Response({"error": f"Произошла ошибка: {str(e)}"}, status=500)

    @action(detail=False, url_path="amenities-tickets")
    def amenities_tickets(self, request):
        items = AmenityTicket.objects.all()
        serializer = AmenityTicketSerializer(items, many=True)
        return Response(serializer.data)
