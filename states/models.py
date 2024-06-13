from django.db import models



class State(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=2)

    def __str__(self):
        return self.name
