from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse

from .forms import AuthorUser
from .models import Author


def create(request):
    print("\n\n\n\n\n\nin the create user...")
    if request.method == 'POST':
        print('post data avaliable')
        authorUser = AuthorUser(request.POST)
        print('authoruser form created')
        if not authorUser.is_valid():
            print('authoruser form is invalid :|')
            print(authorUser.cleaned_data)
            return render(request, 'default/createuser.html', {
                'form' : AuthorUser(),
                'message' : "invalid inputs !!!"
            })
        
        print('data is valid')
        user = User()
        user.username = authorUser.cleaned_data['username']
        user.set_password(authorUser.cleaned_data['password'])
        user.first_name = authorUser.cleaned_data['first_name']
        user.last_name = authorUser.cleaned_data['last_name']
        user.email = authorUser.cleaned_data['email']
        user.is_staff = True
        user.save()
        print('user created')
        author = Author()
        author.display_name = user.username
        author.user = user
        author.save()
        print('author created')
        print('redirecting to login page')
        return HttpResponseRedirect(reverse("login"))
        
        
    
    return render(request, 'default/createuser.html', {
        'form' : AuthorUser(),
        'message' : "enter your information and press create."
    })