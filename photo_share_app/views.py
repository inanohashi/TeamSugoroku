from email.mime import image
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
#モデルインポート
from .models import picture_folder, all_pictures, picture_comment
#フォームをインポート
from .forms import photo_add_form

#写真の一覧を表示するview
def platformview(request):
    #写真のパスをall_picturesテーブルから取得しpicture_listに代入
    picture_list = all_pictures.objects.all()
    return render(request, 'platform/photo_platform.html', {'picture_list':picture_list})

#写真を追加するclass
class platform_addClass(CreateView):
    template_name = 'platform/photo_add_platform.html'
    model = all_pictures #使用するmodel
    form_class = photo_add_form
    success_url = "/photo_share_app/photo_platform"#写真を追加した後の遷移先

'''
無視
def platform_addview (request):

    if request.method == 'POST':
        form = photo_add_form(request.POST, request.FILES)

    if form.is_valid():
        form.save()
        return redirect('photo_platform')

    else:
        form = photo_add_form()
        return render(request, 'platform/photo_add_platform.html', {'form': form})
'''
'''
def platform_addview (request):

    if request.method == 'POST' and request.FILES['images']:

        image = request.FILES['images']
        picture_folderID = request.POST.get('picture_folderID')

        p = all_pictures(
            image = image,
            picture_folderID_id = picture_folderID
            )
        p.save()

    else:
        #folderID = picture_folder()  
        picture_folderID_list = picture_folder.objects.all()
        return render(request, 'platform/photo_add_platform.html', {'picture_folderID_list':picture_folderID_list})
'''





