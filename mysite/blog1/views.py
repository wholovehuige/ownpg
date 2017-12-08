from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.

def index(request):
    articles = models.Article.objects.all()
    return render(request,"blog1/index.html",{'articles':articles})

def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog1/article_page.html',{'article':article})

def edit_page(request,article_id):
    if str(article_id) == '0':
        return render(request,'blog1/edit_page.html')
    article = models.Article.objects.get(pk = article_id)
    return render(request,'blog1/edit_page_save.html',{"article":article})

def edit_action(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    articles = models.Article.objects.all()
    models.Article.objects.create(title=title,content=content)
    return render(request,"blog1/index.html",{'articles':articles})

def article_save(request):
    id = request.POST.get("article_id")
    title = request.POST.get("title")
    content = request.POST.get("content")
    t1 = models.Article(id = id,title = title,content=content)
    t1.save()
    return HttpResponse("<p>数据更新成功</>")

