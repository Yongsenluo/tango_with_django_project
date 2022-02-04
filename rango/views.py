from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Rango say hey there partner!")
