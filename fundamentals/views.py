from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'fundamentals/home.html')
def basics(request):
    return HttpResponse("This is the basics page. Here we will cover the basics of Django.")
def advanced(request):
    return HttpResponse("This is the advanced page. Here we will cover the advanced topics of Django.")
def about(request, name):
    return render(request, 'fundamentals/about.html', {
        'name': name.capitalize()
    })