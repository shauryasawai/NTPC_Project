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

from django.shortcuts import render
from .models import SustainabilityReport, GridBalance
from .utils import calculate_co2_savings, update_grid_balance

def analytics_dashboard(request):
    # Update data
    calculate_co2_savings()
    update_grid_balance()

    # Fetch latest reports
    sustainability_reports = SustainabilityReport.objects.all().order_by('-timestamp')[:10]
    grid_balances = GridBalance.objects.all().order_by('-timestamp')[:10]

    return render(request, "dashboard/analytics.html", {
        "sustainability_reports": sustainability_reports,
        "grid_balances": grid_balances
    })

from django.http import JsonResponse

def sustainability_report_api(request):
    reports = SustainabilityReport.objects.all().order_by('-timestamp')[:10]
    data = [
        {
            "timestamp": str(report.timestamp),
            "total_energy_generated": report.total_energy_generated,
            "fossil_fuel_offset": report.fossil_fuel_offset,
            "co2_reduction": report.co2_reduction
        }
        for report in reports
    ]
    return JsonResponse({"sustainability_reports": data})

def grid_balance_api(request):
    balances = GridBalance.objects.all().order_by('-timestamp')[:10]
    data = [
        {
            "timestamp": str(balance.timestamp),
            "energy_demand": balance.energy_demand,
            "energy_supply": balance.energy_supply,
            "balance": balance.balance
        }
        for balance in balances
    ]
    return JsonResponse({"grid_balance": data})
