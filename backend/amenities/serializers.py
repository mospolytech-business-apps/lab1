from rest_framework import serializers
from amenities.models import AmenityCabinType, AmenityTicket
from amenities.models import Amenity


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = "__all__"


class AmenityTicketSerializer(serializers.ModelSerializer):
    amenity = serializers.SlugRelatedField(slug_field="name", read_only=True)
    ticket = serializers.SlugRelatedField(
        slug_field="booking_reference", read_only=True
    )

    class Meta:
        model = AmenityTicket
        fields = ["id", "amenity", "ticket", "price"]


class AmenityCabinTypeSerializer(serializers.ModelSerializer):
    amenity = serializers.SlugRelatedField(slug_field="name", read_only=True)
    cabin_type = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = AmenityCabinType
        fields = ["id", "amenity", "cabin_type"]
