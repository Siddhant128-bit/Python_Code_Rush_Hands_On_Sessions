# events/views.py
from django.shortcuts import render, redirect
from .forms import EventForm
from .models import Event

def remember_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_events')
    else:
        form = EventForm()
    return render(request, 'events/remember_event.html', {'form': form})

def all_events(request):
    events = Event.objects.all()
    return render(request, 'events/all_events.html', {'events': events})
