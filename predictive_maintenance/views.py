from django.shortcuts import render
from .models import SensorData
from .utils import detect_anomalies

def maintenance_dashboard(request):
    detect_anomalies()  # Update risk scores
    sensors = SensorData.objects.all()
    return render(request, "predictive_maintenance/dashboard.html", {"sensors": sensors})
