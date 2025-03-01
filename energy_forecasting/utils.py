from prophet import Prophet
import pandas as pd
import io

def generate_forecast_from_user_data(csv_file, hours=72):
    """Processes user-uploaded CSV and generates a 72-hour energy forecast."""
    
    try:
        df = pd.read_csv(io.StringIO(csv_file.read().decode("utf-8")))
    except Exception as e:
        print("CSV Read Error:", e)
        return None, None

    # Ensure correct column names
    required_columns = {"timestamp", "solar_output", "wind_output"}
    if not required_columns.issubset(df.columns):
        return None, None

    # Convert timestamp column to datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df.dropna(subset=["timestamp"], inplace=True)  # Remove invalid timestamps
    df = df.sort_values("timestamp")

    # Remove timezone if present
    df["timestamp"] = df["timestamp"].dt.tz_localize(None)

    # Solar Forecasting
    df_solar = df[["timestamp", "solar_output"]].rename(columns={"timestamp": "ds", "solar_output": "y"})
    model_solar = Prophet()
    model_solar.fit(df_solar)

    future_solar = model_solar.make_future_dataframe(periods=hours, freq="H")
    future_solar["ds"] = future_solar["ds"].dt.tz_localize(None)
    forecast_solar = model_solar.predict(future_solar)

    # Wind Forecasting
    df_wind = df[["timestamp", "wind_output"]].rename(columns={"timestamp": "ds", "wind_output": "y"})
    model_wind = Prophet()
    model_wind.fit(df_wind)

    future_wind = model_wind.make_future_dataframe(periods=hours, freq="H")
    future_wind["ds"] = future_wind["ds"].dt.tz_localize(None)
    forecast_wind = model_wind.predict(future_wind)

    return forecast_solar[["ds", "yhat"]], forecast_wind[["ds", "yhat"]]
