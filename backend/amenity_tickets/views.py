from rest_framework.viewsets import ModelViewSet
from .serializers import AmenityTicketSerializer
from .models import AmenityTicket

class AmenityTicketViewset(ModelViewSet):
    queryset=AmenityTicket.objects.all()
    serializer_class=AmenityTicketSerializer