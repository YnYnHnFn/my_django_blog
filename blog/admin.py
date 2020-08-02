from django.contrib import admin

# Register your models here.

# これは自分で定義した Postモデルのインポート
from .models import Post

# Django adminについてもっと知りたいときは、Djangoのドキュメントを見るとよいでしょう。
# https://docs.djangoproject.com/ja/2.0/ref/contrib/admin/


# PostモデルをAdminページ（管理画面）上で見えるようにするために登録。
admin.site.register(Post)

