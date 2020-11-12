from django.contrib import admin
from reqapp01.models import Article

# Register your models here.

class Articleadmin(admin.ModelAdmin):
    list_display = ("title", "author", "ctime")


admin.site.register(Article )