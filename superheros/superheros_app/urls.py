from django.urls import path
from . import views
from django.urls import path
from . import views


app_name = 'superheros_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:superheros_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create_new_superhero')
]

