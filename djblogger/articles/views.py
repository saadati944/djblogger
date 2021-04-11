from django.shortcuts import render
from django.http import HttpResponse


def article(request, article_id):
    return HttpResponse("you have requested article number "+str(article_id))

def create_article(request):
    pass
