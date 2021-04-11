from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    display_name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
       

class Article(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="articles")
    poster = models.ImageField(verbose_name="article_poster")