from email.mime import image
from importlib.resources import contents
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
#モデルインポート
from .models import PictureFolder, AllPictures, PictureComment
#フォームをインポート
from .forms import PhotoAddForm, CreateUserForm

#エラーメッセージ用
from django.contrib import messages
#オーナー用のログイン・ログアウト用
from django.contrib.auth import authenticate, login, logout
#ログインなしではオーナー用フォームに入れない様にする
from django.contrib.auth.decorators import login_required


#サインアップ
def sign_up(request):

    if request.user.is_authenticated:
        #TODO オーナー用プラットフォーム画面に飛ばす
        return redirect('photo_platform')

    else:
        #djangoの認証ユーザーを作っておく
        form = CreateUserForm()

        #POST
        if request.method == "POST":
            form = CreateUserForm(request.POST)

            if form.is_valid():
                form.save()

        context = {'form':form}
        return render(request, 'authority/sign_up.html', context)

#ログイン
def sign_in(request):

    #ログインのキャッシュが残っていたら
    if request.user.is_authenticated:
        #TODO オーナー用プラットフォーム画面に飛ばす
        return redirect('photo_platform')

    #ログイン
    else:
        #POST
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            #ユーザの情報を取得する
            user = authenticate(request, username=username, password=password)
            print(user)

            #認証されたか確認する
            if user is not None:
                login(request, user)
                print(user)

                #TODO オーナー用プラットフォーム画面に飛ばす
                return redirect('photo_platform')
            
            else:
                messages.info(request, 'ユーザーネームまたはパスワードに間違いがあります')
        
        #GET
        return render(request, 'authority/sign_in.html')

#ログアウト
def logout_user(request):
    logout(request)

    return redirect('sign_in')
    
#エラーメッセージ
def errorview(request):
    errormesage = "パスワードが正しくありません"
    return render(request, 'error.html', {'errormessage':errormesage})


def home(request):

    if request.method == "POST":
        id = request.POST.get('id')
        password = request.POST.get('password')



    context = {}
    return render(request, "home.html", context)

#写真の一覧を表示するview
def platformview(request):
    #写真のパスをAllPicturesテーブルから取得しpicture_listに代入
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





#変更試し