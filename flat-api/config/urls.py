
from django.urls import include, path


urlpatterns = [
    path('api/', include('api.urls')),
    path('', include('health_check.urls')),
]