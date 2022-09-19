from email.mime import image
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
#モデルインポート
from .models import PictureFolder, AllPictures, PictureComment, User
#フォームをインポート
from .forms import PhotoAddForm, PlatformAddForm


from .forms import PhotoAddForm, CreateUser


#サインアップ
def sign_up(request):

    if request.POST:
        create_user = CreateUser()
        context = {'create_user':create_user}
        #オーナー用のプラットフォームを作ってもらったら入れる
        return render(request, 'authority/sign_up.html')

    else:    
        return render(request, 'authority/sign_up.html')

#ログイン
def sign_in(request):

    
    return render(request, 'authority/sign_in.html')
    
#エラーメッセージ
def errorview(request):
    errormesage = "パスワードが正しくありません"
    return render(request, 'error.html', {'errormessage':errormesage})

#写真の一覧を表示するview
def platformview(request):
    #写真のパスをall_picturesテーブルから取得しpicture_listに代入
    picture_list = AllPictures.objects.all()
    print(picture_list)
    return render(request, 'platform/photo_platform.html', {'picture_list':picture_list})

#写真を追加するclass
class PlatformAddClass(CreateView):
    template_name = 'platform/photo_add_platform.html'
    model = AllPictures #使用するmodel
    form_class = PhotoAddForm
    success_url = "/photo_share_app/photo_platform"#写真を追加した後の遷移先

#削除する写真を表示するview
def platform_deleteview(request, pk):

    #postされたら画像を削除
    if request.POST:
        #delteする写真をdelte_photoに格納
        delte_photo = AllPictures.objects.get(id=pk)
        delte_photo.delete()

        #写真を削除した後の遷移先
        picture_list = AllPictures.objects.all()
        return render(request, 'platform/photo_platform.html', {'picture_list':picture_list})
    
    #GETの場合の処理
    else:
        photo_path = AllPictures.objects.get(id=pk)
        return render(request, 'platform/photo_delete_platform.html', {'photo_path':photo_path})

def owner_platformview(request):
    folder_list = PictureFolder.objects.all()
    return render(request, 'owner_platform/owner_platform.html', {'folder_list':folder_list})

class OwnerPlatformAddClass(CreateView):
    template_name = 'owner_platform/owner_add_platform.html'
    model = PictureFolder #使用するmodel
    form_class = PlatformAddForm
    success_url = "/owner_platform"#写真を追加した後の遷移先

def owner_platform_deleteview(request, pk):

    #postされたらファイルを削除
    if request.POST:
        #delteするフォルダをdelte_folderに格納
        delte_folder = PictureFolder.objects.get(id=pk)
        delte_folder.delete()

        #フォルダを削除した後の遷移先
        folder_list = PictureFolder.objects.all()
        return render(request, 'owner_platform/owner_platform.html', {'folder_list':folder_list})
    
    #GETの場合の処理
    else:
        platform_path = PictureFolder.objects.get(id=pk)
        return render(request, 'owner_platform/owner_delete_platform.html', {'platform_path':platform_path})


