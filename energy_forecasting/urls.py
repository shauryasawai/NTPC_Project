from django.urls import path
from .views import forecast_view, forecast_api

urlpatterns = [
    path('', forecast_view, name='forecast_view'),
    path('api/', forecast_api, name='forecast_api'),
]
