from django.db import models

class ForecastData(models.Model):
    timestamp = models.DateTimeField()
    solar_output = models.FloatField()
    wind_output = models.FloatField()
