from django.urls import path
from .views import home, map_view

app_name = 'dashboard'

urlpatterns = [
    path('', home, name='home'),
    path('map/', map_view, name='map_view'),
]
