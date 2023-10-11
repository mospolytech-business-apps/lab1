from django.db import models
from countries.models import Country

class Office(models.Model):
    country = models.OneToOneField(Country, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    contact = models.CharField(max_length=255)