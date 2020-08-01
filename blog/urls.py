from django.urls import path
from . import views
# 関数と、blog アプリの全ての ビューをインポートするという意味です。


urlpatterns = [
    path('', views.post_list, name='post_list'),
    #post_list という名前の ビュー をルートURLに割り当て

    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # post/ はURLが post に続けて / で始まることを意味します。ここまでは順調ですね。
    # <int:pk> – この部分はトリッキーです。これはDjangoは整数の値を期待し、その値がpkという名前の変数でビューに渡されることを意味しています。
    # / – それからURLの最後に再び / が必要です。

]