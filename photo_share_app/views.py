from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.shortcuts import render
from django.urls import reverse_lazy
#モデルインポート
#from .models import picture_folder, all_pictures, picture_comment
#フォームをインポート
from .forms import Photoadd


def platformview(request):
    return render(request, 'platform/photo_platform.html')


#def platform_addview (request):




