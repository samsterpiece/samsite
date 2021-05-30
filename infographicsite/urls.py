from django.urls import path
from .views import home
from .views import analyze_data
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', home),
    path('data', analyze_data)
]  + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)