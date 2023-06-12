from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'base/accueil.html')

def devis(request):
    return render(request, 'base/devis.html')
