from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h2>Welcome to SynergyGrid</h2><p><a href='/forecasting/'>Go to Energy Forecasting</a></p>")

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('forecasting/', include('energy_forecasting.urls')),
    path('maintenance/', include('predictive_maintenance.urls')),
    path('dashboard/', include('dashboard.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

