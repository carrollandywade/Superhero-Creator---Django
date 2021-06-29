from django.shortcuts import render
from .models import superhero_app
from django.http import HttpResponse
# Create your views here.


def index(request):
    all_superheros_app = superhero_app.objects.all()
    context = {
        'all_superheros_app': all_superheros_app
    }
    return render(request, 'superheros_app/index.html', context)

