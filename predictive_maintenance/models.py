from django.db import models

class SensorData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    equipment_id = models.CharField(max_length=100)
    temperature = models.FloatField()
    vibration = models.FloatField()
    pressure = models.FloatField()
    failure_risk = models.FloatField(default=0.0)  # Auto-updated by AI model
    latitude = models.FloatField(default=28.7041)  
    longitude = models.FloatField(default=77.1025)

    def __str__(self):
        return f"{self.equipment_id} - {self.timestamp}"
