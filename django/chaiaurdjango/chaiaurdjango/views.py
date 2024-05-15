from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('Hello this is Home Page')
    return render(request, 'index.html')

def about(request):
    return HttpResponse('Hello this is About Page')

def contact(request):
    return HttpResponse('Hello this is Contact Page')