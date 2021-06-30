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


def detail(request, superheros_app_id):
    single_superheros_app = superhero_app.objects.get('<int:superheros_app_id>')
    context = {
        'single_superheros_app': single_superheros_app
    }
    return render(request, superheros_app_id, context)


def create(request):
    if request.method == 'POST':
        name = request.Post.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_superhero_ability = request.POST.get('primary_superhero_ability')
        catchphrase = request.POST.get('catchphrase')
        new_superhero = superhero_app(name=name, genre=alter_ego, runtime=primary_superhero_ability,
                                      release_date=catchphrase)
        new_superhero.save()
        return HttpResponseRedirect(reverse('superheros:index'))
    else:
        return render(request, 'superheros/create.html')
