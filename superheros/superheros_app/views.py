from django.shortcuts import render
from .models import superhero_app
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
# Create your views here.


def index(request):
    all_superheros_app = superhero_app.objects.all()
    context = {
        'all_superheros_app': all_superheros_app
    }
    return render(request, 'superheros_app/index.html', context)


def detail(request, superheros_id):
    single_superheros_app = superhero_app.objects.get(id=superheros_id)
    context = {
        'single_superheros_app': single_superheros_app
    }
    return render(request, 'superheros_app/detail.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_superhero_ability = request.POST.get('primary_superhero_ability')
        secondary_superhero_ability = request.POST.get('secondary_superhero_ability')
        catchphrase = request.POST.get('catchphrase')
        new_superhero = superhero_app(name=name,
                                      alter_ego=alter_ego,
                                      primary_superhero_ability=primary_superhero_ability,
                                      secondary_superhero_ability=secondary_superhero_ability,
                                      catchphrase=catchphrase)
        new_superhero.save()
        return HttpResponseRedirect(reverse('superheros_app:index'))
    else:
        return render(request, 'superheros_app/create.html')


def update(request, superheros_id):
    single_superheros_app = superhero_app.objects.get(id=superheros_id)
    context = {
        'single_superheros_app': single_superheros_app
    }
    return render(request, 'superheros_app/update.html', context)

