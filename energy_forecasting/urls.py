from django.urls import path
from .views import user_forecast_view

urlpatterns = [
    path('', user_forecast_view, name='user_forecast'),
]
