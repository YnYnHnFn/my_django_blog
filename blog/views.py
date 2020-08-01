from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.

# ビューはただのPythonの関数です。

def post_list(request):

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'blog/post_list.html', {'posts': posts})
    # blog/post_list.html テンプレートを（色々なものを合わせて）
    # 組み立てる render という関数を呼び出して得た値を 
    # return しています。

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
