from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Topic, List
from django.utils import timezone


def index(request):
    topic_list = Topic.objects.order_by('issued_date')
    context = {'topic_list': topic_list}
    return render(request, 'jotlists/index.html', context)


def remove_list(request, list_id):
    try:
        list_name = List.objects.get(pk=list_id)
    except (KeyError, List.DoesNotExist):
        return render(request, 'jotlists/index.html', {
            'topic_list': Topic.objects.order_by('issued_date'),
            'error_message': "Such a list does not exist!",
        })
    else:
        list_name.delete()
        return HttpResponseRedirect(reverse('jotlists:index', args=()))


def remove_topic(request, topic_id):
    try:
        topic_name = Topic.objects.get(pk=topic_id)
    except (KeyError, Topic.DoesNotExist):
        return render(request, 'jotlists/index.html', {
            'topic_list': Topic.objects.order_by('issued_date'),
            'error_message': "Such a topic does not exist!",
        })
    else:
        topic_name.delete()
        return HttpResponseRedirect(reverse('jotlists:index', args=()))


def create_list(request):
    try:
        task = List(list_text=request.POST['list_text'], topic_title=Topic.objects.get(pk=request.POST['topic_title']))
        if task.list_text is "":
            raise KeyError
    except KeyError:
        return render(request, 'jotlists/index.html', {
            'topic_list': Topic.objects.order_by('issued_date'),
            'error_message': "Can't create an item with no name!",
        })
    else:
        task.save()
        return HttpResponseRedirect(reverse('jotlists:index', args=()))


def create_topic(request):
    try:
        topic = Topic(topic_name=request.POST['topic_name'], issued_date=timezone.now())
        if topic.topic_name is "":
            raise KeyError
    except KeyError:
        return render(request, 'jotlists/index.html', {
            'topic_list': Topic.objects.order_by('issued_date'),
            'error_message': "Can't create a topic with no name!",
        })
    else:
        topic.save()
        return HttpResponseRedirect(reverse('jotlists:index', args=()))
