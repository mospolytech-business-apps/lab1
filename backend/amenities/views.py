from rest_framework.viewsets import ModelViewSet
from .serializers import AmenitySerializer
from .models import Amenity

class AmenityViewset(ModelViewSet):
    queryset=Amenity.objects.all()
    serializer_class=AmenitySerializer