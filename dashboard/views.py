from django.shortcuts import render
from energy_forecasting.models import ForecastData
from predictive_maintenance.models import SensorData

def home(request):
    # Get latest energy forecast
    forecasts = ForecastData.objects.all().order_by('-timestamp')[:10]

    # Get latest equipment health data
    sensors = SensorData.objects.all().order_by('-timestamp')[:10]

    return render(request, "dashboard/home.html", {"forecasts": forecasts, "sensors": sensors})


def map_view(request):
    # Pass sensor data for map visualization
    sensors = SensorData.objects.all()
    return render(request, "dashboard/map.html", {"sensors": sensors})
