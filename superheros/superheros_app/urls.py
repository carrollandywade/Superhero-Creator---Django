from django.urls import path
from . import views
from django.urls import path
from . import views


app_name = 'superheros_app'
urlpatterns = [
    path('', views.index, name='index')
]
