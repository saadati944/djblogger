from django.urls import path
from .views import article

app_name = 'articles'

urlpatterns = [
    path('<int:article_id>/', article, name='article')
]
