from dataclasses import field
from .models import PictureFolder, AllPictures, PictureComment, User
from django import forms

#djangoのauth User用
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



#オーナー用のユーザーテーブル用のフォーム
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



#写真を追加するフォーム
class PhotoAddForm(forms.ModelForm):
    class Meta:
        model = AllPictures
        fields = ('images','picture_folderID')
        labels = {'images':'画像'}

    class PlatformAddForm(forms.ModelForm):
        class Meta:
            model = PictureFolder
            fields = ('picture_folder_name', 'piture_folder_password')
            labels = {'picture_folder_name':'タイトル', 'piture_folder_password':'パスワード'}

<<<<<<< HEAD

class CreateUser(forms.ModelForm):
    class Meta:
        model =  User
        fields = ('username', 'email', 'password')
        labels = {
            'username': 'Username',
            'email' : 'Email address',
            'password' : 'Password'
        }


class PlatformAddForm(forms.ModelForm):
    class Meta:
        model = PictureFolder
        fields = ('picture_folder_name', 'piture_folder_password')
        labels = {'picture_folder_name':'タイトル', 'piture_folder_password':'パスワード'}

=======
>>>>>>> 07a6b8669f986630e86b8bb98a28ca9cc404840a
