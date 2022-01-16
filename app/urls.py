from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from app.views import app, home, upload

urlpatterns = [
    path('', home, name='home'),
    path('app/', app, name='app'),
    path('app/upload/', upload, name='upload'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)