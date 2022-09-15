from .models import picture_folder, all_pictures, picture_comment
from django import forms

class Photoadd(forms.ModelForm):
    class Meta:
        model = all_pictures
        fields = ('images',)
        labels = {'images':'画像'}
