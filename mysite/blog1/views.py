from django.shortcuts import render
from . import models
# Create your views here.

def index(request):
    articles = models.Article.objects.all()
    return render(request,"blog1/index.html",{'articles':articles})

def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog1/article_page.html',{'article':article})
