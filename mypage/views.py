# helloapp/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def kinki(request):
    return render(request, 'kinki.html')

def wakayama(request):
    return render(request, 'wakayama.html')

