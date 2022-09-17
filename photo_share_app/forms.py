from .models import PictureFolder, AllPictures, PictureComment, User
from django import forms

#写真を追加するフォーム
class PhotoAddForm(forms.ModelForm):
    class Meta:
        model = AllPictures
        fields = ('images','picture_folderID')
        labels = {'images':'画像'}


class CreateUser(forms.ModelForm):
    class Meta:
        model =  User
        fields = ('username', 'email', 'password')
        labels = {
            'username': 'Username',
            'email' : 'Email address',
            'password' : 'Password'
        }