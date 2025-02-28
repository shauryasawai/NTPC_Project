from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ForecastData
import pandas as pd
from prophet import Prophet
from .forms import DataUploadForm

# Energy Forecasting View
def forecast_view(request):
    # Fetch historical data
    data = ForecastData.objects.all()
    
    if not data.exists():
        return HttpResponse("No historical data available for forecasting.")

    # Convert to DataFrame
    df = pd.DataFrame(list(data.values()))
    df['ds'] = df['timestamp']  # Prophet requires 'ds' for date
    df['y'] = df['solar_output']  # Prophet requires 'y' as target variable

    # Train Prophet Model
    model = Prophet()
    model.fit(df[['ds', 'y']])

    # Predict for the next 72 hours
    future = model.make_future_dataframe(periods=72, freq='H')
    forecast = model.predict(future)

    # Convert forecast results to dictionary
    forecast_data = forecast[['ds', 'yhat']].to_dict(orient='records')

    return render(request, "energy_forecasting/forecast.html", {"forecast_data": forecast_data})


# Upload Data for Forecasting
def upload_data(request):
    if request.method == "POST":
        form = DataUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_csv(file)

            # Ensure required columns exist
            if {'timestamp', 'solar_output', 'wind_output'}.issubset(df.columns):
                # Convert timestamp to datetime
                df['timestamp'] = pd.to_datetime(df['timestamp'])

                # Save data to database
                for _, row in df.iterrows():
                    ForecastData.objects.create(
                        timestamp=row['timestamp'],
                        solar_output=row['solar_output'],
                        wind_output=row['wind_output']
                    )

                return HttpResponse("Data uploaded successfully!")

            else:
                return HttpResponse("Invalid CSV format. Required columns: timestamp, solar_output, wind_output.")
    else:
        form = DataUploadForm()

    return render(request, "energy_forecasting/upload.html", {"form": form})
