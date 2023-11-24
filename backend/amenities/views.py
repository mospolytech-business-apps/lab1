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

    @action(detail=False, url_path="amenities-statistics")
    def amenities_statistics(self, request):
        amenities = Amenity.objects.values_list("name", flat=True)
        statistics = []

        cabin_types = CabinType.objects.all()
        for cabin_type in cabin_types:
            data = []
            for amenity in amenities:
                count = Ticket.objects.filter(
                    cabin_type=cabin_type, amenityticket__amenity__name=amenity
                ).count()
                data.append(count)

            statistics.append({"class": cabin_type.name, "data": data})

        response_data = {"amenities": list(amenities), "statistics": statistics}

        return Response(response_data)

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
