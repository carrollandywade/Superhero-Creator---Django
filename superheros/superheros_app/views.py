from django.shortcuts import render
from .models import superhero_app
from django.http import HttpResponse
# Create your views here.


def index(request):
    all_superheros = superhero_app.objects.all()
    context = {
        'all_superheros': all_superheros
    }
    return render(request, 'superheros_app/index.html')
