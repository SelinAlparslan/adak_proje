# Generated by Django 3.2 on 2021-05-28 18:08

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_contactformmessage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactFormMessage',
        ),
        migrations.AddField(
            model_name='setting',
            name='tuzuk',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]
