from django.db import models

class Amenity(models.Model):
    Service = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.Service} - ${self.Price}"
