from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import platformview, platform_addClass, platform_deleteview



urlpatterns = [
    path('photo_platform/', platformview, name='photo_platform'),
    path('photo_add_platform/', platform_addClass.as_view(), name='photo_add_platform'),
    #pkにall_picturesテーブルのidを格納
    path('photo_delete_platform/<int:pk>', platform_deleteview, name='photo_delete_platform'),
    
]\
+ static (settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
