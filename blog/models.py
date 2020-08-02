from django.db import models

# Create your models here.
from django.utils import timezone

# モデルのフィールドや上記以外の定義のやり方について知りたい方は是非Djangoドキュメントを見てみて下さい。 
# https://docs.djangoproject.com/ja/2.0/ref/models/fields/#field-types)

class Post(models.Model):
# Post はモデルの名前で、他の名前をつけることもできます。モデルの名前は大文字で始めます。
# models.Model はポストがDjango Modelだという意味で、
# Djangoが、「これはデータベースに保存すべきものだ」と分かるようにしています。

    # 各項目

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    text = models.TextField()   # これは制限無しの長いテキスト

    created_date = models.DateTimeField(default=timezone.now)

    published_date = models.DateTimeField(blank=True, null=True)


    # 各処理

    def publish(self):
    # ブログを公開するメソッド
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#### ---------- ---------- ---------- ---------- 
#### - データベースにモデルと対になるテーブルを作成する。
#### - models.py にモデルのクラスを作ったら、DBにそれを知らせないとイカン！
#### 
#### -- 1)manage.py に対して モデルに変化があったことを伝えて、
#### -- migrations/の下にDB変更用のファイルを作る。
#### ommand-line
#### myvenv) ~/djangogirls$ python manage.py makemigrations blog
#### igrations for 'blog':
#### log/migrations/0001_initial.py:　＜＜＜＜これ
#### 
####  Create model Post
#### 
#### 
#### -- 2)でもって、そのファイル（自動的に判断してくれる）を使って
#### ommand-line
#### myvenv) ~/djangogirls$ python manage.py migrate blog
#### perations to perform:
#### pply all migrations: blog
#### unning migrations:
#### pplying blog.0001_initial... OK  ＜＜＜ 上で作られたファイルがOKになっている。
#### 