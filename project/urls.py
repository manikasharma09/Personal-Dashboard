from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('ToDo', include('todolists.urls')),
    path('RemindMe', include('reminders.urls')),
    path('JotItDown', include('jotlists.urls')),
    path('admin', admin.site.urls),
]
