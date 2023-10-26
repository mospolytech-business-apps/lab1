from rest_framework import serializers
from .models import AmenityTicket


class AmenityTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model= AmenityTicket
        fields ='__all__'
        