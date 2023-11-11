from django.db import models
from amenities.models import Amenity
from сabintyps.models import CabinType  

class AmenityCabinType(models.Model):
    AmenityID = models.ForeignKey(Amenity, on_delete=models.CASCADE)
    CabinTypeID = models.ForeignKey(CabinType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.AmenityID} - {self.CabinTypeID}"
