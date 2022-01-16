from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from .views import login, logout, signup

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout', logout, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)