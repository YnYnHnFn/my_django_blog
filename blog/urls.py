from django.urls import path
from . import views

# mysite/urls.py で「ここに行け」と書いてあるので、ここに来る。

# Django URLconfについてもっと知りたい場合は、公式のドキュメントを見て下さい
# https://docs.djangoproject.com/ja/2.0/topics/http/urls/

urlpatterns = [

    # post_list という名前の ビュー をルートURLに割り当てています。
    # このパターンは誰かがあなたのWebサイトの 'http://127.0.0.1:8000/' というアドレス
    # にアクセスしてきたら views.post_list が正しい行き先だということをDjangoに伝えます。
    # '' はトップの階層を表している。＝ 'http://127.0.0.1:8000/'（※ローカルの場合）
    # 最後の name='post_list' は、ビューを識別するために使われる URLの名前です。
    # htmlのテンプレートの中とかで識別したくなる。

    # トップ画面、は一覧
    path('', views.post_list, name='post_list'),

    # 新規投稿画面へ
    path('post/new/', views.post_new, name='post_new'),

    # 詳細ページへ
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # 'post/         ' 　：
    #       <int:pk>/'   ： Djangoは整数の値を期待し、その値がpkという名前の変数でビューに渡されることを意味しています。
    # views.post_detail　： URLが上のパタンにマッチしたときは post_detail というViewにいきなはれ。
    # name='post_detail' ： テンプレートで私を書くときは「post_detail」って名前を使ってくれ。

    # 編集できる詳細ページへ
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

]
