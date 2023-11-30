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

    @action(detail=False, methods=['post'], url_path="amenities-statistics")
    def amenities_statistics(self, request):
        booking_reference = request.data.get('booking_reference')
        if not booking_reference:
            return Response({"error": "Booking reference is required."}, status=400)

        try:
            ticket = Ticket.objects.get(booking_reference=booking_reference)
        except Ticket.DoesNotExist:
            return Response({"error": "Ticket not found."}, status=404)

        amenities_data = AmenityTicket.objects.filter(ticket=ticket).values(
            'amenity__service', 'ticket__first_name', 'ticket__last_name', 'ticket__passport_number'
        )

        return Response({"class": ticket.cabin_type.name, "data": list(amenities_data)})
    

    @action(detail=False, methods=['post'], url_path="amenity-report")
    def amenity_report(self, request):
        flight_id = request.data.get('flight_id')
        departure_airport = request.data.get('departure_airport')
        arrival_airport = request.data.get('arrival_airport')

        if not flight_id or not departure_airport or not arrival_airport:
            return Response({"error": "Flight ID, departure airport, and arrival airport are required."}, status=400)

        try:
            schedule = Schedule.objects.get(pk=flight_id)
            tickets = Ticket.objects.filter(schedule=schedule)
            tickets = tickets.filter(
                schedule__Route__DepartureAirport=departure_airport,
                schedule__Route__ArrivalAirport=arrival_airport
            )

            amenities_data = AmenityTicket.objects.filter(ticket__in=tickets).values(
                'amenity__service', 'ticket__cabin_type'
            )

            # Format data as specified
            amenities = [item['amenity__service'] for item in amenities_data]
            statistics = {}
            for item in amenities_data:
                if item['ticket__cabin_type'] not in statistics:
                    statistics[item['ticket__cabin_type']] = [0, 0, 0, 0]

                if item['amenity__service'] == 1:
                    statistics[item['ticket__cabin_type']][0] += 1
                elif item['amenity__service'] == 2:
                    statistics[item['ticket__cabin_type']][1] += 1
                elif item['amenity__service'] == 3:
                    statistics[item['ticket__cabin_type']][2] += 1
                elif item['amenity__service'] == 4:
                    statistics[item['ticket__cabin_type']][3] += 1

            result = {
                "amenities": amenities,
                "statistics": [
                    {"class": key, "data": value} for key, value in statistics.items()
                ]
            }

            return Response(result)

        except Schedule.DoesNotExist:
            return Response({"error": "Flight not found."}, status=404)
        except Exception as e:
            return Response({"error": f"An error occurred: {str(e)}"}, status=500)

    @action(detail=False, url_path="amenities-cabin-type")
    def amenities_cabin_type(self, request):
        items = AmenityCabinType.objects.all()
        serializer = AmenityCabinTypeSerializer(items, many=True)
        return Response(serializer.data)

    @action(detail=False, url_path="amenities-tickets")
    def amenities_tickets(self, request):
        items = AmenityTicket.objects.all()
        serializer = AmenityTicketSerializer(items, many=True)
        return Response(serializer.data)
