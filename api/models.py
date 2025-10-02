from django.db import models

# Create your models here.
from django.db import models

class Localizacao(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.latitude}, {self.longitude} - {self.timestamp}"
