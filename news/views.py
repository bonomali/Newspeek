from django.shortcuts import render
from django.http import HttpResponse
from news.modules.articlefinder import *
from .models import Greeting

# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        article = ArticleFinder(request.POST.get("article", ''), request.POST.get("question", ''))  
        print("Data being sent to client")
        print(article.finalURL)
        return HttpResponse(article.finalURL)

def post(request):
    pass

#def db(request):

#    greeting = Greeting()
#    greeting.save()

#    greetings = Greeting.objects.all()

#    return render(request, 'db.html', {'greetings': greetings})

