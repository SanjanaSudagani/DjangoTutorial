from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, this is Sanjana Sudagani. This is my first Django App.")