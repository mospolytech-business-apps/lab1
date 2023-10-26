from rest_framework import serializers
from .models import AmenityCabinType


class AmenityCabinTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model= AmenityCabinType
        fields ='__all__'
        