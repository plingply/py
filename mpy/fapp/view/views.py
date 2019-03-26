from django.shortcuts import render

# coding:utf-8
from django.http import HttpResponse
from fapp.models import Xiaohua
def index(request):
    return HttpResponse(u"欢迎光临 自强学堂!")

def welcome(request):
    
    page = int(request.GET.get('page')) - 1 if(request.GET.get('page')) else 0
    limit = int(request.GET.get('limit')) if(request.GET.get('limit')) else 10 

    start = page*limit
    end = start + limit

    xlist = Xiaohua.objects.all()[start : end ]
    return render(request, 'welcome.html',{
        'title' : '欢迎',
        'list' : xlist
    })
