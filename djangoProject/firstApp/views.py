from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(response):
    return HttpResponse("<h1>My first Django Application</h1>\nSetting up my first Django App")
