from django.urls import path
from .views import article, create_article

app_name = 'articles'

urlpatterns = [
    path('<int:article_id>/', article.as_view(), name='article'),
    path('create/', create_article.as_view(), name='create')
]
