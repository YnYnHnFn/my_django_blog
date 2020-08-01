from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

# モデルフィールドリファレンス
# https://docs.djangoproject.com/ja/2.2/ref/models/fields/#field-types


"""
models.CharField – 文字数が制限されたテキストを定義するフィールド
models.TextField – これは制限無しの長いテキスト用です。ブログポストのコンテンツに理想的なフィールドでしょ？
models.DateTimeField – 日付と時間のフィールド
models.ForeignKey – これは他のモデルへのリンク
"""

#モデルの名前は大文字で始めます。
#models.Model>> これはデータベースに保存すべきものだと分かるようにしています。
class Post(models.Model):
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=200)
    
    text = models.TextField()
    
    created_date = models.DateTimeField(default=timezone.now)
    
    published_date = models.DateTimeField(blank=True, null=True)

    # これこそが先程お話ししたブログを公開するメソッドそのものです。
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title