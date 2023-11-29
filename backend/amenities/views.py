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


class AmenityViewSet(viewsets.ModelViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer

    @action(detail=False, methods=['post'], url_path="amenities-statistics")
    def amenities_statistics(self, request):
        ticket_id = request.data.get('ticket_id')
        if not ticket_id:
            return Response({"error": "Ticket ID is required."}, status=400)

        try:
            ticket = Ticket.objects.get(pk=ticket_id)
        except Ticket.DoesNotExist:
            return Response({"error": "Ticket not found."}, status=404)

        amenities_data = AmenityTicket.objects.filter(ticket=ticket).values(
            'amenity__service', 'ticket__firstname', 'ticket__lastname', 'ticket__passport_number'
        )

        return Response({"class": ticket.cabin_type.name, "data": list(amenities_data)})

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
