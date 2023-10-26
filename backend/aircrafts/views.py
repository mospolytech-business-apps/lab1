from rest_framework.viewsets import ModelViewSet
from .serializers import AircraftSerializer
from .models import Aircraft

class AircraftViewset(ModelViewSet):
    queryset=Aircraft.objects.all()
    serializer_class=AircraftSerializer