from django.urls import path

from . import views

app_name = 'todolists'

urlpatterns = [
    path('', views.index, name='index'),
    path('/<int:task_id>/remove', views.remove, name='remove'),
    path('/create', views.create, name='create'),
]