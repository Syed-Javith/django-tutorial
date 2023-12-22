from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def say_hello(request):
    return HttpResponse("hello")

def hello_template(request):
    return render( request , "hello.html" )

def home(request,name):
    return HttpResponse(name)