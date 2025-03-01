from django.contrib import admin
from energy_forecasting.models import EnergyData
from predictive_maintenance.models import SensorData

admin.site.register(EnergyData)
admin.site.register(SensorData)
