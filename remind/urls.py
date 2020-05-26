from django.urls import path

from . import views

app_name = 'reminders'
urlpatterns = [
    path('', views.index, name='index'),
    path('/add', views.add, name='add'),
    path('/create', views.create, name='create'),
    path('/<int:reminder_id>/remove', views.remove, name='remove'),
    path('/<int:reminder_id>/', views.detail, name='detail'),
]
