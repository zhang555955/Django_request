# Generated by Django 3.0 on 2020-11-11 03:10

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='文章标题')),
                ('author', models.CharField(max_length=32, verbose_name='文章作者')),
                ('ctime', models.DateField(verbose_name='发表日期')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='文章内容')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='文章描述')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='文章描述')),
            ],
        ),
    ]
