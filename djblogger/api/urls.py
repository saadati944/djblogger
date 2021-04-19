from django.urls import path
from .views import articles_collection

urlpatterns = [
    path('articles', articles_collection, name='articles_collection')
]
