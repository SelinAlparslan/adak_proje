from django.db import models
from django.utils.safestring import mark_safe 
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm, TextInput, Textarea
# Create your models here.
class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(max_length=150, blank = True)
    phone = models.CharField(max_length=15, blank = True)
    email = models.CharField(max_length=25, blank = True)
    icon = models.ImageField(blank= True, upload_to='images/')
    facebook = models.CharField(max_length=50, blank = True)
    twitter = models.CharField(max_length=50, blank = True)
    instagram = models.CharField(max_length=50, blank = True)
    aboutus = models.CharField(max_length=255, blank = True)
    contact = models.CharField(max_length=255, blank = True)
    status = models.CharField(max_length=10, choices = STATUS)
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now= True)
    tuzuk = RichTextUploadingField(blank=True)

    def __str__(self):
        return self.title
    
class Images(models.Model):
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField( upload_to='images/')
    detail = RichTextUploadingField(blank=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description ='Image'


