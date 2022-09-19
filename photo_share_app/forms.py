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

#オーナー用のプラットフォーム追加用のフォーム
class PlatformAddForm(forms.ModelForm, id):
    class Meta:
        model = PictureFolder
        fields = ('ownerID', 'picture_folder_name', 'piture_folder_password')
        labels = {'ownerID': 'ownerID','picture_folder_name':'タイトル', 'piture_folder_password':'パスワード'}


#写真を追加するフォーム
class PhotoAddForm(forms.ModelForm):
    class Meta:
        model = AllPictures
        fields = ('images','picture_folderID')
        labels = {'images':'画像'}

