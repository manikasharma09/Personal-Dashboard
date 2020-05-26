from django.urls import path

from . import views

app_name = 'jotlists'
urlpatterns = [
    path('', views.index, name='index'),
    path('/<int:list_id>/remove_list', views.remove_list, name='remove_list'),
    path('/<int:topic_id>/remove_topic', views.remove_topic, name='remove_topic'),
    path('/create_list', views.create_list, name='create_list'),
    path('/create_topic', views.create_topic, name='create_topic'),
]
