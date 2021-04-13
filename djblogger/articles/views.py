from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Author


def article(request, article_id):
    art = None
    art = Article.objects.filter(id = article_id).first()
    if art == None :
        # tdoo : 
        return render(request, "default/articlenotfound.html", {
            'id':article_id
        })
    return render(request, 'default/viewer.html', {
        'title' : art.title,
        'author' : art.author,
        'date_created' : art.date_created,
        'content' : art.content
    })

def create_article(request):
    pass
