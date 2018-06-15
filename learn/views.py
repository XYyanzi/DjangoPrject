#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("hello Django！")


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add3(request):
    return render(request, 'learn/home1.html')


def show_string(request):
    string = u'我在自强学堂学习Django，用它来建网站'
    return render(request, 'learn/string.html', {'string': string})


def show_list(request):
    TutorialList = ['python', 'django', 'html', 'css', 'jQuery']
    return render(request, 'learn/list.html', {'TutorialList': TutorialList})


def show_dict(request):
    info_dict = {"site": u"自强学堂", "content": u"各种IT技术教程"}
    return render(request, 'learn/dict.html', {'info_dict': info_dict})


def show_for(request):
    List = map(str, range(100))  # 一个长度为100的 List
    return render(request, 'learn/for.html', {'List': List})


def show_if(request):
    var = 78
    return render(request, 'learn/ifelse.html', {'var': var})

