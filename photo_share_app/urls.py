from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import platformview


urlpatterns = [
    path('photo_platform/', platformview),
    path('photo_add_platform/', platformview),
    path('photo_delete_platform/', platformview),
    
]\
+ static (settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)