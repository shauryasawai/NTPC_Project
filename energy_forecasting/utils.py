import pandas as pd
from prophet import Prophet
from .models import EnergyData

def generate_forecast(hours=72):
    """Generates a 72-hour energy forecast using Prophet"""
    
    data = EnergyData.objects.all().values('timestamp', 'solar_output', 'wind_output')
    df = pd.DataFrame(list(data))
    
    if df.empty:
        return None, None

    # Remove timezone from timestamp
    df['timestamp'] = df['timestamp'].dt.tz_localize(None)

    # Forecast Solar Output
    df_solar = df[['timestamp', 'solar_output']].rename(columns={'timestamp': 'ds', 'solar_output': 'y'})
    model_solar = Prophet()
    model_solar.fit(df_solar)
    
    future_solar = model_solar.make_future_dataframe(periods=hours, freq='h')
    future_solar['ds'] = future_solar['ds'].dt.tz_localize(None)  # Remove timezone
    forecast_solar = model_solar.predict(future_solar)
    
    # Forecast Wind Output
    df_wind = df[['timestamp', 'wind_output']].rename(columns={'timestamp': 'ds', 'wind_output': 'y'})
    model_wind = Prophet()
    model_wind.fit(df_wind)
    
    future_wind = model_wind.make_future_dataframe(periods=hours, freq='h')
    future_wind['ds'] = future_wind['ds'].dt.tz_localize(None)  # Remove timezone
    forecast_wind = model_wind.predict(future_wind)
    
    return forecast_solar[['ds', 'yhat']], forecast_wind[['ds', 'yhat']]
