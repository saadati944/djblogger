from django.db import models
from users.models import Author
from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="articles")
    poster = models.ImageField(verbose_name="poster")
    content = RichTextUploadingField(blank=False,null=False, default="<h1>Empty Article !!!</h1>")

    def __str__(self):
        return f"{self.title} @ {self.date_created} by {self.author}"