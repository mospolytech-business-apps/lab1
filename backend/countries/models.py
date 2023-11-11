from django.db import models

class Country(models.Model):
    Name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.Name}"