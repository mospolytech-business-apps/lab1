from rest_framework.viewsets import ModelViewSet
from .serializers import AmenitySerializer
from .models import Amenity
from сabintyps.models import CabinType
from tickets.models import Ticket
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response

class AmenityViewset(ModelViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer

    @action(detail=False, url_path="amenities-statistics")
    def amenities_statistics(self, request):
        amenities = Amenity.objects.values_list('Service', flat=True)
        statistics = []
        for cabin_type in CabinType.objects.all():
            data = [
                Ticket.objects.filter(CabinTypeID=cabin_type, amenities__Service=amenity).count()
                for amenity in amenities
            ]
            statistics.append({
                'class': cabin_type.name,
                'data': data,
            })
        response_data = {
            'amenities': list(amenities),
            'statistics': statistics,
        }

        return Response(response_data)
