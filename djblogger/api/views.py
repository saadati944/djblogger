from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import serializers
from articles.models import Article
from django.views import View

class ArticleSerializer(serializers.ModelSerializer):
    url = 'sd'
    class Meta:
        model = Article
        fields = ('id', 'author', 'title', 'date_created', 'poster')

@api_view(['GET'])
def articles_collection(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

