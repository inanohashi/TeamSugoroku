from django.contrib import admin
from django.urls import path
from .views import sign_up_Class, sign_in_Class
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign_up/', sign_up_Class.as_view()),
    path('sign_in/', sign_in_Class.as_view()),
]+ static (settings.STATIC_URL, document_root=settings.STATIC_ROOT)
