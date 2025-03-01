
from django.db import models

class SustainabilityReport(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    total_energy_generated = models.FloatField()  # MW
    fossil_fuel_offset = models.FloatField()  # MW replaced by renewable energy
    co2_reduction = models.FloatField()  # kg of CO2 saved

    def __str__(self):
        return f"CO2 Reduction Report - {self.timestamp}"

class GridBalance(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    energy_demand = models.FloatField()  # MW
    energy_supply = models.FloatField()  # MW
    balance = models.FloatField()  # Difference (positive = surplus, negative = shortage)

    def save(self, *args, **kwargs):
        self.balance = self.energy_supply - self.energy_demand
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Grid Balance - {self.timestamp}"
