from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print ('hola hola hola')
    print ('hola hola hola')
    print ('hola hola hola')
    print ('hola hola hola')
    print ('hola hola hola')
    print ('hola hola hola')

    return HttpResponse("<h2>Hello world!!! this is a django site. Hola Danny!!!</h2>")
