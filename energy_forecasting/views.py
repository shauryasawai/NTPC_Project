import pandas as pd
from django.shortcuts import render
from .forms import UploadCSVForm
from .utils import generate_forecast_from_user_data
from django.http import HttpResponseBadRequest

import pandas as pd
from django.shortcuts import render
from django.http import HttpResponseBadRequest
from .forms import UploadCSVForm
from .utils import generate_forecast_from_user_data

def user_forecast_view(request):
    if request.method == "POST":
        print("request.FILES:", request.FILES)  # Debugging: Check if file is received

        form = UploadCSVForm(request.POST, request.FILES)

        if "csv_file" not in request.FILES:  # Debugging: Check if 'csv_file' exists
            return HttpResponseBadRequest("Error: No file uploaded!")

        if form.is_valid():
            csv_file = request.FILES["csv_file"]
            forecast_solar, forecast_wind = generate_forecast_from_user_data(csv_file)

            if forecast_solar is None or forecast_wind is None:
                return render(request, "energy_forecasting/no_data.html", {"message": "Invalid CSV format!"})

            return render(request, "energy_forecasting/user_forecast.html", {
                "solar_labels": [str(d) for d in forecast_solar["ds"]],
                "solar_data": [float(d) for d in forecast_solar["yhat"]],
                "wind_labels": [str(d) for d in forecast_wind["ds"]],
                "wind_data": [float(d) for d in forecast_wind["yhat"]],
            })
    
    else:
        form = UploadCSVForm()

    return render(request, "energy_forecasting/upload.html", {"form": form})



from django.http import JsonResponse

def forecast_api(request):
    forecast_solar, forecast_wind = generate_forecast_from_user_data()

    if forecast_solar is None or forecast_wind is None:
        return JsonResponse({"error": "No data available"}, status=404)

    return JsonResponse({
        "solar_forecast": forecast_solar.to_dict(orient="records"),
        "wind_forecast": forecast_wind.to_dict(orient="records"),
    })
