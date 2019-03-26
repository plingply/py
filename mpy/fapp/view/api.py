
# coding:utf-8
from django.http import JsonResponse
from django.core import serializers
from fapp.models import Xiaohua

def getlist(request):
    
    page = int(request.GET.get('page')) - 1 if(request.GET.get('page')) else 0
    limit = int(request.GET.get('limit')) if(request.GET.get('limit')) else 10 

    start = page*limit
    end = start + limit

    xlist = Xiaohua.objects.all()[start : end ]

    result = serializers.serialize("json",xlist)
    
    return JsonResponse({
        'status':'ok',
        'mgs':'列表',
        'code': 1,
        'data': result
    })
