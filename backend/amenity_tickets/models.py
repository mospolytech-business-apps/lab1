from django.db import models
from amenities.models import Amenity
from tickets.models import Ticket 

class AmenityTicket(models.Model):
    AmenityID = models.ForeignKey(Amenity, on_delete=models.CASCADE)
    TicketID = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    Price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.AmenityID} - {self.TicketID}"
