from django.contrib import admin
from .models import picture_folder, all_pictures, picture_comment
# Register your models here.

admin.site.register(picture_folder)
admin.site.register(all_pictures)
admin.site.register(picture_comment)
