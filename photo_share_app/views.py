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

#削除画面を表示するview
def platform_deleteview(request, pk):

    #postされたら画像を削除
    if request.POST:
        #delete_yes_buttonが押されたとき
        if "delete_yes_button" in request.POST:
            #delteする写真をdelte_photoに格納して削除
            delte_photo = all_pictures.objects.get(id=pk)
            delte_photo.delete()

            #写真を削除した後の遷移先
            picture_list = all_pictures.objects.all()
            return render(request, 'platform/photo_platform.html', {'picture_list':picture_list})

        #delete_no_buttonが押されたとき
        elif "delete_no_button" in request.POST:
            #写真を削除しないときの遷移先
            picture_list = all_pictures.objects.all()
            return render(request, 'platform/photo_platform.html', {'picture_list':picture_list})

    #GETの場合の処理
    else:
        photo_path = all_pictures.objects.get(id=pk)
        return render(request, 'platform/photo_delete_platform.html', {'photo_path':photo_path})
