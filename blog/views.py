from django.shortcuts import render

# Create your views here.

# ビューはただのPythonの関数です。

def post_list(request):

    return render(request, 'blog/post_list.html', {})
    # blog/post_list.html テンプレートを（色々なものを合わせて）
    # 組み立てる render という関数を呼び出して得た値を 
    # return しています。
