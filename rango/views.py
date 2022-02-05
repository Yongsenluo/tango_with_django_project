from pydoc import html
from re import A
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Rango says hey there partner! \
        <br/> <a href='/rango/about/'>about</a>")

def about(request):
    return HttpResponse("Rango say here is the about page\
        <br/> <a href='/rango/'> index</a>")