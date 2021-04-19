from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse

from django.contrib.auth import authenticate, get_user, login, logout

from articles.models import Article

from .forms import AuthorUser
from .models import Author


def create(request):
    if request.method == 'POST':

        authorUser = AuthorUser(request.POST)
        if not authorUser.is_valid():
            return render(request, 'default/createuser.html', {
                'form' : AuthorUser(),
                'message' : "invalid inputs !!!"
            })
        
        user = User()
        user.username = authorUser.cleaned_data['username']
        user.set_password(authorUser.cleaned_data['password'])
        user.first_name = authorUser.cleaned_data['first_name']
        user.last_name = authorUser.cleaned_data['last_name']
        user.email = authorUser.cleaned_data['email']
        user.is_staff = True
        user.save()

        author = Author()
        author.display_name = user.username
        author.user = user
        author.save()

        return HttpResponseRedirect(reverse("login"))
        
        
    
    return render(request, 'default/createuser.html', {
        'form' : AuthorUser(),
        'message' : "enter your information and press create."
    })

def all_articles(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    author = Author.objects.get(user = request.user)

    #todo : don't show all articles of a user in one page.
    articles = author.articles.all()
    return render(request, 'default/allarticles.html', {
        'articles' : articles
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
