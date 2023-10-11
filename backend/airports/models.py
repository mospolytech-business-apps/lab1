from django.db import models
from countries.models import Country

class Airport(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    IATACode = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.IATACode} - {self.name}"
