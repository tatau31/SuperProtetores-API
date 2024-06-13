from django.db import models
from cities.models import City


class Institution(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='institutions')
    description = models.TextField()

    def __str__(self):
        return self.name
