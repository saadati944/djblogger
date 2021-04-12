from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class Author(models.Model):
    display_name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.display_name} ({self.user})"
       

class Article(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="articles")
    poster = models.ImageField(verbose_name="article_poster")
    content = RichTextUploadingField(blank=False,null=False, default="<h1>Empty Article !!!</h1>")

    def __str__(self):
        return f"{self.title} @ {self.date_created} by {self.author}"