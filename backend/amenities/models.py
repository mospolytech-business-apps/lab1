from django.db import models
from tickets.models import Ticket
from cabintypes.models import CabinType


class Amenity(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=19, decimal_places=4)

    def __str__(self):
        return self.name


class AmenityCabinType(models.Model):
    cabin_type = models.ForeignKey(CabinType, on_delete=models.CASCADE)
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("cabin_type", "amenity")


class AmenityTicket(models.Model):
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=19, decimal_places=4, default=0.0000)

    class Meta:
        unique_together = ("amenity", "ticket")
