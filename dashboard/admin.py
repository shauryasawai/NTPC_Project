from django.contrib import admin
from energy_forecasting.models import ForecastData
from predictive_maintenance.models import SensorData

admin.site.register(ForecastData)
admin.site.register(SensorData)
