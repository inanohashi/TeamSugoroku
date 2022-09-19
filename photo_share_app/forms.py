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

