from django.shortcuts import render
from django.http import HttpResponse
from modules.articlefinder import *
from .models import Greeting

# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        article = ArticleFinder(request.data["article"], request.data["question"])
        return render(request, 'index.html', {"url": article.finalURL})


#def db(request):

#    greeting = Greeting()
#    greeting.save()

#    greetings = Greeting.objects.all()

#    return render(request, 'db.html', {'greetings': greetings})

