import numpy as np
import pandas as pd
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import MinMaxScaler
from .models import SensorData

def train_autoencoder():
    data = SensorData.objects.all().values('temperature', 'vibration', 'pressure')
    df = pd.DataFrame(list(data))

    if df.empty:
        return None

    scaler = MinMaxScaler()
    X = scaler.fit_transform(df)

    model = Sequential([
        Dense(8, activation='relu', input_shape=(3,)),
        Dense(4, activation='relu'),
        Dense(8, activation='relu'),
        Dense(3, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='mse')
    model.fit(X, X, epochs=50, verbose=0)

    return model, scaler

def detect_anomalies():
    model, scaler = train_autoencoder()
    if model is None:
        return

    data = SensorData.objects.all()
    df = pd.DataFrame(list(data.values('id', 'temperature', 'vibration', 'pressure')))
    X_scaled = scaler.transform(df[['temperature', 'vibration', 'pressure']])

    X_pred = model.predict(X_scaled)
    reconstruction_loss = np.mean(np.abs(X_scaled - X_pred), axis=1)

    for i, obj in enumerate(data):
        obj.failure_risk = reconstruction_loss[i]
        obj.save()
