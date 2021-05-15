from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('This is home page')

def about(request):
    return HttpResponse('This is about page')

def service(request):
    return HttpResponse('This is service page')

def contact(request):
    return HttpResponse('This is contact page')