from django import forms
from .models import Article
from django.contrib.auth import get_user
from django.contrib.auth.models import User

class ArticleContent(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'poster']
