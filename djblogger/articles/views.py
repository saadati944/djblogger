from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, get_user, login, logout
from django.contrib.auth.models import User
from .models import Article, Author
from .forms import ArticleContent


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
        'content' : art.content,
        'poster' : art.poster.url
    })

def create_article(request):
    #force user to sign in to be able to create articles
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    #create new article with post data, save it and show it.
    if(request.method == "POST"):
        
        form_content = ArticleContent(request.POST, request.FILES)
        
        if not form_content.is_valid():
            return render(request, 'default/addarticle.html', {
                'form' : ArticleContent(),
                'message' : 'invalid information !!'
            })

        art = Article()
        art.title = form_content.cleaned_data['title']
        art.content = form_content.cleaned_data['content']
        art.author = Author.objects.get(user = request.user)
        art.poster = form_content.cleaned_data['poster']

        art.save()
        
        return HttpResponseRedirect(reverse('articles:article', args=(art.id, )))

    #return addarticle.html file if there isn't any post data
    return render(request, 'default/addarticle.html', {
        'form' : ArticleContent(),
        'message' : 'enter information then press save'
    })


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # todo : create an index page and redirect to it
            return HttpResponseRedirect(reverse("articles:create"))
        else:
            return render(request, "default/login.html",{
                'message': "incorrect credentials !!!"
            })

    return render(request, "default/login.html",{
        'message':'enter username and password'
    })

def logout_view(request):
    logout(request)
    return render(request, "default/login.html",{
        'message':'logged out'
    })
