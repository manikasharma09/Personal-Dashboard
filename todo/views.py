from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todo
from django.utils import timezone


def index(request):
    todo_list = Todo.objects.order_by('-added_date')
    context = {'todo_list': todo_list}
    return render(request, 'todolists/index.html', context)


def remove(request, task_id):
    try:
        task = Todo.objects.get(pk=task_id)
    except (KeyError, Todo.DoesNotExist):
        return render(request, 'todolists/index.html', {
            'todo_list': Todo.objects.order_by('-added_date'),
            'error_message': "Such a task does not exist!",
        })
    else:
        task.delete()
        return HttpResponseRedirect(reverse('todolists:index', args=()))


def create(request):
    try:
        task = Todo(text=request.POST['task_text'], added_date=timezone.now())
        if task.text is "":
            raise KeyError
    except KeyError:
        return render(request, 'todolists/index.html', {
            'todo_list': Todo.objects.order_by('-added_date'),
            'error_message': "Can't create an empty task.",
        })
    else:
        task.save()
        return HttpResponseRedirect(reverse('todolists:index', args=()))

