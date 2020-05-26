from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Reminder
from django.utils import timezone


def index(request):
    reminder_past = Reminder.objects.filter(end_date__lte=timezone.now()).order_by('-issued_date')
    reminder_upcoming = Reminder.objects.filter(start_date__gte=timezone.now()).order_by('-issued_date')
    reminder_live = Reminder.objects.filter(start_date__lte=timezone.now()).filter(
                    end_date__gte=timezone.now()).order_by('-issued_date')
    context = {'reminder_past': reminder_past, 'reminder_upcoming': reminder_upcoming, 'reminder_live': reminder_live}
    return render(request, 'reminders/index.html', context)


def detail(request, reminder_id):
    reminder = get_object_or_404(Reminder, pk=reminder_id)
    return render(request, 'reminders/detail.html', {'reminder': reminder})


def create(request):
    try:
        reminder = Reminder(text=request.POST['reminder_text'], topic_name=request.POST['topic_title'],
                            description=request.POST['description'],
                            start_date=request.POST['start_date'], end_date=request.POST['end_date'])
        reminder.issued_date = timezone.now()
        if reminder.start_date >= reminder.end_date:
            raise KeyError
    except KeyError:
        reminder_past = Reminder.objects.filter(end_date__lte=timezone.now()).order_by('-issued_date')
        reminder_upcoming = Reminder.objects.filter(start_date__gte=timezone.now()).order_by('-issued_date')
        reminder_live = Reminder.objects.filter(start_date__lte=timezone.now()).filter(
            end_date__gte=timezone.now()).order_by('-issued_date')
        context = {'reminder_past': reminder_past, 'reminder_upcoming': reminder_upcoming,
                   'reminder_live': reminder_live, 'error_message': "Invalid input!"}
        return render(request, 'reminders/index.html', context)
    else:
        reminder.save()
        return HttpResponseRedirect(reverse('reminders:index', args=()))


def add(request):
    return render(request, 'reminders/add.html', {})


def remove(request, reminder_id):
    try:
        reminder = Reminder.objects.get(pk=reminder_id)
    except (KeyError, Reminder.DoesNotExist):
        reminder_past = Reminder.objects.filter(end_date__lte=timezone.now()).order_by('-issued_date')
        reminder_upcoming = Reminder.objects.filter(start_date__gte=timezone.now()).order_by('-issued_date')
        reminder_live = Reminder.objects.filter(start_date__lte=timezone.now()).filter(
            end_date__gte=timezone.now()).order_by('-issued_date')
        context = {'reminder_past': reminder_past, 'reminder_upcoming': reminder_upcoming,
                   'reminder_live': reminder_live, 'error_message': "Such a topic does not exist!"}
        return render(request, 'reminders/index.html', context)
    else:
        reminder.delete()
        return HttpResponseRedirect(reverse('reminders:index', args=()))
