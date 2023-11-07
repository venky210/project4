from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def developers(request):
    return HttpResponse('<marquee>hii developers how are you</marquee>')
