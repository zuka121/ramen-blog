# helloapp/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def hokkaido(request):
    return render(request, 'hokkaido.html')

def tohoku(request):
    return render(request, 'tohoku.html')

def kanto(request):
    return render(request, 'kanto.html')

def tyubu(request):
    return render(request, 'tyubu.html')

def kinki(request):
    return render(request, 'kinki.html')

def tyugoku(request):
    return render(request, 'tyugoku.html')

def shikoku(request):
    return render(request, 'shikoku.html')

def kyusyu(request):
    return render(request, 'kyusyu.html')

def profile(request):
    return render(request, 'profile.html')

def wakayama(request):
    return render(request, 'wakayama.html')

def shimasyo(request):
    return render(request, 'shimasyo.html')
