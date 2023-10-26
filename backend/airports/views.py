from rest_framework.viewsets import ModelViewSet
from .serializers import AirportSerializer
from .models import Airport

class AirportViewset(ModelViewSet):
    queryset=Airport.objects.all()
    serializer_class=AirportSerializer