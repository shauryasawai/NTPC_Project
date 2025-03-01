from django.urls import path
from .views import home, map_view, analytics_dashboard, sustainability_report_api, grid_balance_api

app_name = 'dashboard'

urlpatterns = [
    path('', home, name='home'),
    path('map/', map_view, name='map_view'),

    # Analytics Dashboard
    path('analytics/', analytics_dashboard, name='analytics_dashboard'),

    # API Endpoints
    path('api/sustainability/', sustainability_report_api, name='sustainability_report_api'),
    path('api/grid_balance/', grid_balance_api, name='grid_balance_api'),
]
