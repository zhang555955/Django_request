from django.shortcuts import render

# Create your views here.
from reqapp01.models import Article
from django.core.paginator import Paginator

def req(request):
    return render(request, 'request.html', {"req": dir(request),"request":request})


def articlelist(request):
    page = request.GET.get('p')
    articledata = Article.objects.all()
    #实例化Paginator,叫它对所查到对的所有文章进行分页，每3条一页
    paging = Paginator(articledata, 2)   #数据队列
    pagedata =paging.page(page) #单页的数据

    return render(request,'index.html', locals())

def article(request):
    if request.method == 'GET' and request.GET:
        idnum = int(request.GET.get('id'))
        art = Article.objects.get(id=idnum)
    return render(request, 'article.html', locals())