from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def home(request):
    return HttpResponse("Olá, Mundo!")

def lista_post(request):
    lista_de_posts = Post.objects.all()
    return render(request,'posts.html',  {'lista_de_posts': lista_de_posts})

