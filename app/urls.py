from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from app.views import app, home

urlpatterns = [
    path('', home, name='home'),
    path('app/', app, name='app')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)