from django.db import models

class EnergyData(models.Model):
    timestamp = models.DateTimeField()
    solar_output = models.FloatField()
    wind_output = models.FloatField()
    temperature = models.FloatField()
    wind_speed = models.FloatField()

    def __str__(self):
        return f"{self.timestamp} - Solar: {self.solar_output}, Wind: {self.wind_output}"
