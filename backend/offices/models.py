from django.db import models
from countries.models import Country

class Office(models.Model):
    CountryID = models.OneToOneField(Country, on_delete=models.CASCADE)
    Title = models.CharField(max_length=255)
    Phone = models.CharField(max_length=20)
    Contact = models.CharField(max_length=255)