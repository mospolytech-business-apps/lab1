from rest_framework.viewsets import ModelViewSet
from .serializers import AmenityCabinTypeSerializer
from .models import AmenityCabinType

class AmenityCabinTypeViewset(ModelViewSet):
    queryset=AmenityCabinType.objects.all()
    serializer_class=AmenityCabinTypeSerializer