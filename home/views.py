from django.shortcuts import redirect, render, HttpResponse

def index(request):
    #return HttpResponse('This is home page')
    context = {
        'variable1':"Maharashtra is state",
        'variable2':"India is country"
    }
    return render(request, 'index.html', context)

def about(request):
    return HttpResponse('This is about page')

def service(request):
    return HttpResponse('This is service page')

def contact(request):
    return HttpResponse('This is contact page')