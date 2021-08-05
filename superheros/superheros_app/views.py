from django.shortcuts import render
from .models import superhero_app
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.forms import ModelForm
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
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


def update(request, superheros_id):
    single_superheros_app = superhero_app.objects.get(id=superheros_id)
    context = {
        'single_superheros_app': single_superheros_app
    }
    if request.method == 'POST':
        single_superheros_app.name = request.POST.get('name')
        single_superheros_app.alter_ego = request.POST.get('alter_ego')
        single_superheros_app.primary_superhero_ability = request.POST.get('primary_superhero_ability')
        single_superheros_app.secondary_superhero_ability = request.POST.get('secondary_superhero_ability')
        single_superheros_app.catchphrase = request.POST.get('catchphrase')
        single_superheros_app.save()
        return HttpResponseRedirect(reverse('superheros_app:index'))
    else:
        return render(request, 'superheros_app/update.html', context)


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


def kryptonite(request, superheros_id):
    superhero_app.objects.filter(id=superheros_id).delete()
    return HttpResponseRedirect(reverse('superheros_app:index'))

