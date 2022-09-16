from .models import picture_folder, all_pictures, picture_comment
from django import forms

#写真を追加するフォーム
class photo_add_form(forms.ModelForm):
    class Meta:
        model = all_pictures
        fields = ('images','picture_folderID')
        labels = {'images':'画像'}


