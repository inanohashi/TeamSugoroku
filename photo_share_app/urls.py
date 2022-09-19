from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import PlatformAddClass


urlpatterns = [

    #ホーム画面
    path('', views.home, name = 'home'),

    #オーナー用のsign out, sign in, logout
    path('sign_up/', views.sign_up, name = 'sign_up'),
    path('sign_in/', views.sign_in, name = 'sign_in'),
    path('logout/', views.logout_user, name = 'logout'),

    #写真プラットフォーム
    path('photo_platform/', views.platformview, name='photo_platform'),
    path('photo_add_platform/', PlatformAddClass.as_view(), name='photo_add_platform'),
    #pkにall_picturesテーブルのidを格納
    path('photo_delete_platform/<int:pk>', views.platform_deleteview, name='photo_delete_platform'),
    
]\
+ static (settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
