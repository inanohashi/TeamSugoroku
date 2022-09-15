from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.shortcuts import render
#モデルインポート
from .models import picture_folder, all_pictures, picture_comment

def platformview(request):
    return render(request, 'platform/photo_platform.html')


#class platform_addClass (CreateView):



