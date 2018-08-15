from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def my404(req):
    return render(req,'error/404.html')


def my500(req):
    return render(req, 'error/500.html')

def computer(request):
    a = 100/0
    # return HttpResponse('ok')
    return render(request, 'a.html')