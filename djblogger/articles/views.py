from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, get_user, login, logout
from django.contrib.auth.models import User
from .models import Article, Author
from .forms import PostForm


def article(request, article_id):
    art = None
    art = Article.objects.filter(pk = article_id).first()
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
        'poster' : art.poster
    })

def create_article(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    if(request.method == "POST"):
        #todo:validating postform data doesn't work !!!
        form_data = PostForm(request.POST, request.FILES)
        if(not form_data.is_valid()):
            pass
            #todo:check why form data is always invalid !
        aut = Author.objects.filter(user = request.user).first()
        art = Article()
        art.title = form_data.cleaned_data['title']
        art.content = form_data.cleaned_data['content']
        art.author = aut
        art.save()
        return HttpResponseRedirect(reverse('articles:article', args=(art.id, )))

    return render(request, 'default/addarticle.html', {
        'form' : PostForm()
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
