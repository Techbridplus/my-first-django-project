from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
    # return HttpResponse('Hello world')
    x=1
    y=2
    return render(request,'hello.html',{'name':'gaurav Joshi'})
