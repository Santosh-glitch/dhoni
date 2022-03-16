from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dhoni(request):
    return HttpResponse('dhoni best Captain')

def raina(request):
    return HttpResponse('<marquee><h1>Raina is Mr.IPL</h1></marquee>')
