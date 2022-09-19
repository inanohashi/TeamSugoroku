from django.contrib import admin
from .models import User, PictureFolder, AllPictures, PictureComment
# Register your models here.

admin.site.register(User)
admin.site.register(PictureFolder)
admin.site.register(AllPictures)
admin.site.register(PictureComment)
