from django.contrib import admin
from home.models import Setting, Images


# Register your models here.

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'detail']



admin.site.register(Setting)
admin.site.register(Images, ImagesAdmin)
