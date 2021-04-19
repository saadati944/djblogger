from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, get_user, login, logout
from django.contrib.auth.models import User
from django.views import View
from .models import Article
from users.models import Author
from .forms import ArticleContent

class article(View):
    def get(self, request, article_id):
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

class create_article(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))

        return render(request, 'default/addarticle.html', {
            'form' : ArticleContent(),
            'message' : 'enter information then press save'
        })
    
    def post(self, request):
        if(request.method != "POST"):
            # todo : do something better !!!
            return HttpResponse("ERROR !!!")
        
        form_content = ArticleContent(request.POST, request.FILES)
        
        if not form_content.is_valid():
            return render(request, 'default/addarticle.html', {
                'form' : ArticleContent(),
                'message' : 'invalid information !!'
            })

        art = form_content.save(commit=False)
        art.author = Author.objects.get(user = request.user)
        art.save()

        return HttpResponseRedirect(reverse('articles:article', args=(art.id, )))



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
