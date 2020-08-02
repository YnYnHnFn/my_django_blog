from django import forms
from .models import Post

# 自作のモデル(今回ではPostモデル)用のdjangoフォームをつくる。

class PostForm(forms.ModelForm):
# ModelForm として使用できるように forms.ModelForm を継承します

    class Meta: # インナークラスとして class Meta を定義し、

        # Djangoにフォームを作るときにどのモデル（テーブル）を使えばいいかを伝えます。
        model = Post

        # フォームのフィールドに何の項目を置くか書きます。
        fields = ('title', 'text',)
        # author、created_date は自動で入るようにするので、フォームには入れない。

