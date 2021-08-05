from django.urls import path
from . import views


app_name = 'superheros_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:superheros_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create_new_superhero'),
    path('update/<int:superheros_id>/', views.update, name='update'),
    path('kryptonite/<int:superheros_id>', views.kryptonite, name='kryptonite')
]

