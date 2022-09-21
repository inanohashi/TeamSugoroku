from email.mime import image
from importlib.resources import contents
from urllib import request
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, FormView
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
#モデルインポート
from .models import PictureFolder, AllPictures, PictureComment
#フォームをインポート
from .forms import PhotoAddForm, CreateUserForm, PlatformAddForm

#エラーメッセージ用
from django.contrib import messages
#オーナー用のログイン・ログアウト用
from django.contrib.auth import authenticate, login, logout
#ログインなしではオーナー用フォームに入れない様にする
from django.contrib.auth.decorators import login_required


#ホームページ
def home(request):
    return render(request, 'home.html')

#写真フォルダーへログイン
def photos_share_login(request):

    if request.method == "POST":
        picture_folder_name = request.POST.get('platform_name')
        piture_folder_password = request.POST.get('password')

        queryset = PictureFolder.objects.filter(picture_folder_name = picture_folder_name, piture_folder_password = piture_folder_password)

        try:
            print(queryset[0].pk)
            request.session['folder_id'] = queryset[0].pk
            return redirect('photo_platform')
        
        except:
            messages.info(request, '名前またはパスワードが間違っています')
            return redirect('')
            


    context = {}
    return render(request, "platform/platform_login.html", context)


#サインアップ
def sign_up(request):

    if request.user.is_authenticated:
        #TODO オーナー用プラットフォーム画面に飛ばす
        user_id = request.user.id
        request.session['user_id'] = user_id
        return redirect('owner_platform')

    else:
        #djangoの認証ユーザーを作っておく
        form = CreateUserForm()

        #POST
        if request.method == "POST":
            form = CreateUserForm(request.POST)

            if form.is_valid():
                form.save()
                return redirect('sign_in')

        context = {'form':form}
        return render(request, 'authority/sign_up.html', context)

#ログイン
def sign_in(request):

    #ログインのキャッシュが残っていたら
    if request.user.is_authenticated:
        #TODO オーナー用プラットフォーム画面に飛ばす
        user_id = request.user.id
        request.session['user_id'] = user_id
        return redirect('owner_platform')

    #ログイン
    else:
    #POST
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            #ユーザの情報を取得する
            user = authenticate(request, username=username, password=password)

            #認証されたか確認する
            if user is not None:
                login(request, user)
                user_id = user.id
                request.session['user_id'] = user_id
                
                #オーナー用プラットフォーム画面に飛ばす
                return redirect('owner_platform')
            
            else:
                messages.info(request, 'ユーザーネームまたはパスワードに間違いがあります')
    
    #GET
    return render(request, 'authority/sign_in.html')

#ログアウト
def logout_user(request):
    request.session.clear()
    logout(request)

    return redirect('sign_in')

def logout_platform(request):
    request.session.clear()
    return redirect('')
    
#エラーメッセージ
def errorview(request):
    errormesage = "パスワードが正しくありません"
    return render(request, 'error.html', {'errormessage':errormesage})

#オーナー用プラットフォーム
def owner_platformview(request):
    user_id = request.session['user_id']
    folder_list = PictureFolder.objects.filter(ownerID = user_id)
    return render(request, 'owner_platform/owner_platform.html', {'folder_list':folder_list})

#オーナー用写真フォルダ（写真プラットフォーム）作成
def owner_platform_add_photos(request):
    form =  PlatformAddForm()

    if request.method =="POST":
        user_id = request.session['user_id']
        # form =  PlatformAddForm({**request.POST, 'ownerID':user_id})
        a = PictureFolder(ownerID = user_id)
        form = PlatformAddForm(request.POST, instance=a)
        form.save()
        return redirect('owner_platform')

    context = {'form':form}
    return render(request, 'owner_platform/owner_add_platform.html', context)

#オーナー用写真フォルダ(写真プラットフォーム) 削除
def owner_platform_deleteview(request, pk):
    
    #postされたらファイルを削除
    if request.POST:
        #delteするフォルダをdelte_folderに格納
        delte_folder = PictureFolder.objects.get(id=pk)
        delte_folder.delete()
        return redirect ('owner_platform')
    
    #GETの場合の処理
    else:
        platform_path = PictureFolder.objects.get(id=pk)
        return render(request, 'owner_platform/owner_delete_platform.html', {'platform_path':platform_path})


#写真の一覧を表示するview
def platformview(request):
    #写真のパスをAllPicturesテーブルから取得しpicture_listに代入
    picture_folder_id = request.session['folder_id']
    picture_list = AllPictures.objects.filter(picture_folderID = picture_folder_id)
    print(picture_list)
    return render(request, 'platform/photo_platform.html', {'picture_list':picture_list})

#写真を追加するclass
class PlatformAddClass(CreateView):
    
    template_name = 'platform/photo_add_platform.html'
    model = AllPictures #使用するmodel
    form_class = PhotoAddForm
    success_url = "/photo_platform"#写真を追加した後の遷移先


   
#削除画面を表示するview
def platform_deleteview(request, pk):

    #postされたら画像を削除
    if request.POST:
        #delete_yes_buttonが押されたとき
        if "delete_yes_button" in request.POST:
            #delteする写真をdelte_photoに格納して削除
            delte_photo = AllPictures.objects.get(id=pk)
            delte_photo.delete()

            #写真を削除した後の遷移先
            return redirect('photo_platform')

        #delete_no_buttonが押されたとき
        elif "delete_no_button" in request.POST:
            #写真を削除しないときの遷移先
            return redirect('photo_platform')

    #GETの場合の処理
    else:
        photo_path = AllPictures.objects.get(id=pk)
        return render(request, 'platform/photo_delete_platform.html', {'photo_path':photo_path})
