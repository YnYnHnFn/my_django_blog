from django.contrib import admin
from .models import Post #定義したPostモデルをimportしています。

# Register your models here.

admin.site.register(Post)