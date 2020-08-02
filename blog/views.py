from django.shortcuts import render
# Create your views here.
from django.shortcuts import get_object_or_404

# 新しく作成された記事の post_detail ページを表示できれば良いですよね? そのために次のインポートを追加します:
from django.shortcuts import redirect

from django.utils import timezone

from .models import Post    ### 自分で作ったモデル（構造体宣言）
from .forms import PostForm ### 自分で作ったフォーム（登録用のクラス？）


# Djangoのビューについてもっと知りたい場合
# https://docs.djangoproject.com/ja/2.0/topics/http/views/

# Djangoのクエリセットについてもっと知りたい場合
# https://docs.djangoproject.com/ja/2.0/ref/models/querysets/

# Djangoのフォームについてもっと知りたい場合
# https://docs.djangoproject.com/ja/2.0/topics/forms/


### ---------- ---------- ---------- ---------- 
### 一覧画面
### ---------- ---------- ---------- ---------- 
def post_list(request):

    # request を引数に取り、blog/post_list.htmlテンプレートを組み立てる render 関数を return しています。
    # これが一番単純な形式
  # return render(request, 'blog/post_list.html', {})

    # ↓↓↓↓ 

    #クエリセット使って 絞って並べる。
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    # 降順ソートは order_by にマイナス

    # htmlを生成して返します！
    return render(request, 'blog/post_list.html', {'posts': posts})
    # render()の引数説明
    # 　request：インターネットを介してユーザから受け取った全ての情報が詰まったものです。
    # 　'blog/post_list.html'：テンプレートはこれ。
    # 　{'posts': posts}：テンプレートの中で、'posts'って名前で変数postsの中身を使ってね。

### ---------- ---------- ---------- ---------- 
### 1件表示
### ---------- ---------- ---------- ---------- 
def post_detail(request, pk):

    #Post モデルを get_object_or_404() で取得
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'blog/post_detail.html', {'post': post})

### ---------- ---------- ---------- ---------- 
### 1件新規追加
### ---------- ---------- ---------- ---------- 
def post_new(request):

    if request.method == "POST":

        # PostFormクラスのインスタンスを作成
        form = PostForm(request.POST)

        if form.is_valid():
        # フォームの値が正しいかどうかをチェックします
        # （すべての必須フィールドが設定され、不正な値が送信されないこと）。

            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            # 入力が終わったときは post_detail に移動する。ここで終わり。
            return redirect('post_detail', pk=post.pk) 
    else:

        # PostFormクラスのインスタンスを作成
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form': form})

### ---------- ---------- ---------- ---------- 
### 1件更新
### ---------- ---------- ---------- ---------- 
def post_edit(request, pk):
# 既存データの編集の場合、pk パラメータが URLに追加されている。

    #編集したいPost モデルを get_object_or_404() で取得
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":

        # get_object_or_404()で取得したpostを インスタンスとして指定してFormを作る。
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
        # フォームの値が正しいかどうかをチェックします
        # （すべての必須フィールドが設定され、不正な値が送信されないこと）。

            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            # 入力が終わったときは post_detail に移動する。ここで終わり。
            return redirect('post_detail', pk=post.pk)
    else:
        # このポストを編集するためにただフォームを開く場合も
        # get_object_or_404()で取得したpostを インスタンスとして指定してFormを作る。

        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {'form': form})
