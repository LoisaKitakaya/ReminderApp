from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from .views import about, app, contacts, delete, done, home, upload

urlpatterns = [
    path('', home, name='home'),
    path('app/', app, name='app'),
    path('app/upload/', upload, name='upload'),
    path('app/about/', about, name='about'),
    path('app/contacts', contacts, name='contacts'),
    path('app/done/<id>', done, name='done'),
    path('app/delete/<id>', delete, name='delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)