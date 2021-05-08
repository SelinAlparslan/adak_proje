from django.contrib import admin
from home.models import Setting, Images, ContactFormMessage


# Register your models here.

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'detail']

class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'status']
    list_filter = ['status']

admin.site.register(Setting)
admin.site.register(Images, ImagesAdmin)
admin.site.register(ContactFormMessage, ContactFormMessageAdmin)