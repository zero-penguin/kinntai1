from django import forms

from .models import Post

# このフォームが ModelForm の一種だとDjangoに伝える
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)