from django.contrib import admin
from Core.models import *
# Register your models here.

class UploadImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'uploadTime')
    list_filter = ('uploadTime',)
    search_fields = ('id', 'image', 'uploadTime')

admin.site.register(UploadImage, UploadImageAdmin)
