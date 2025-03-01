from django.shortcuts import render
from energy_forecasting.models import EnergyData
from predictive_maintenance.models import SensorData

def home(request):
    # Get latest energy forecast
    forecasts = EnergyData.objects.all().order_by('-timestamp')[:10]

    # Get latest equipment health data
    sensors = SensorData.objects.all().order_by('-timestamp')[:10]

    return render(request, "dashboard/home.html", {"forecasts": forecasts, "sensors": sensors})


def map_view(request):
    # Pass sensor data for map visualization
    sensors = SensorData.objects.filter(failure_risk__gt=0.30)
    return render(request, "dashboard/map.html", {"sensors": sensors})
