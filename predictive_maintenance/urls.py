from django.urls import path
from .views import maintenance_dashboard

urlpatterns = [
    path('', maintenance_dashboard, name='maintenance_dashboard'),
]
