from django.urls import path
from .views import create, all_articles

app_name = 'users'

urlpatterns = [
    path('create/', create, name="create"),
    path('articles/', all_articles, name="articles")
]
