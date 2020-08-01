from django.urls import path
from . import views
# 関数と、blog アプリの全ての ビューをインポートするという意味です。


urlpatterns = [
    path('', views.post_list, name='post_list'),
    #post_list という名前の ビュー をルートURLに割り当て


]