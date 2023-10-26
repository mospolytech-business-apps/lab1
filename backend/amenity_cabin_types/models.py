from django.db import models
from amenities.models import Amenity
from сabintyps.models import CabinType  

class AmenityCabinType(models.Model):
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)
    cabin_type = models.ForeignKey(CabinType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.amenity} - {self.cabin_type}"
