from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Event
from .forms import EventForm

def remember_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/events')
    else:
        form = EventForm()
    return render(request, 'event_manager/remember_event.html',{'form':form})
def all_events(request):
    events = Event.objects.all()
    return render(request,'event_manager/all_events.html',{'events':events})


