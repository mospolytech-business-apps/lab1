from django.db import models
from amenities.models import Amenity
from tickets.models import Ticket 

class AmenityTicket(models.Model):
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.amenity} - {self.ticket}"
