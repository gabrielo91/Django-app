from django.shortcuts import render
from django.http import HttpResponse

def index():
    return HttpResponse("Hello world! this is a django site")