from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def index(request):
    return HttpResponse('caonima')

def add(request):
    a = request.GET.get('a',0)
    b = request.GET.get('b',0)
    c = int(a) + int(b)
    return HttpResponse(str(c))