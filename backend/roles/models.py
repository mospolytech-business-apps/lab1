from django.db import models

class Role(models.Model):
    Title = models.CharField(max_length=255)