from django.shortcuts import render
from .utils import generate_forecast

def forecast_view(request):
    forecast_solar, forecast_wind = generate_forecast()

    if forecast_solar is None or forecast_wind is None:
        return render(request, "energy_forecasting/no_data.html")

    return render(request, "energy_forecasting/forecast.html", {
        "solar_labels": [str(d) for d in forecast_solar["ds"]],
        "solar_data": [float(d) for d in forecast_solar["yhat"]],
        "wind_labels": [str(d) for d in forecast_wind["ds"]],
        "wind_data": [float(d) for d in forecast_wind["yhat"]],
    })

from django.http import JsonResponse

def forecast_api(request):
    forecast_solar, forecast_wind = generate_forecast()

    if forecast_solar is None or forecast_wind is None:
        return JsonResponse({"error": "No data available"}, status=404)

    return JsonResponse({
        "solar_forecast": forecast_solar.to_dict(orient="records"),
        "wind_forecast": forecast_wind.to_dict(orient="records"),
    })
