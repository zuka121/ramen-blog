# forms.py
from django import forms
from .models import Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        labels = {
            'username': 'ユーザー名',
            'password1': 'パスワード',
            'password2': 'パスワード（確認用）',
        }

def clean_username(self):
        username = self.cleaned_data.get('username')
        
        # 全角文字を含む正規表現でバリデーション
        if not re.match(r'^[\w.@+-\u3000-\u303F\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]+$', username):
            raise forms.ValidationError("ユーザー名には日本語の全角文字、英数字、@/./+/-/_ のみを使用できます。")
        
        # 既存のユーザー名との重複チェック
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("このユーザー名はすでに使われています。")
        
        return username
