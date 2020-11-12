from django.db import models

# Create your models here.
from ckeditor_uploader.fields import RichTextUploadingField

class Article(models.Model):
    title = models.CharField(max_length=32,verbose_name="文章标题")
    author = models.CharField(max_length=32,verbose_name="文章作者")
    ctime = models.DateField(verbose_name="发表日期")
    content = RichTextUploadingField(verbose_name="文章内容")
    description = RichTextUploadingField(verbose_name="文章描述")
    picture = models.ImageField(upload_to="images", blank=True, null=True, verbose_name="文章描述")

    def __str__(self):
        return self.title