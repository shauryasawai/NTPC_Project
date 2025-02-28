from django.urls import path
from .views import forecast_view, upload_data

app_name = 'energy_forecasting'

urlpatterns = [
    path('', forecast_view, name='forecast'),
    path('upload/', upload_data, name='upload_data'),
]
