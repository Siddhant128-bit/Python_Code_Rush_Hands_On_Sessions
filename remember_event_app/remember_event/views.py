from django.shortcuts import render,redirect
from .models import Event
from django.http import HttpResponse
from .mail import send_email


def home(request):
    return render(request, 'home.html')

def remember(request):
    if request.method=="POST":
        recipient_email=request.POST.get('recipient_email')
        send_datetime=request.POST.get('send_datetime')
        message_content=request.POST.get('message_content')
        print(send_datetime)
        Event.objects.create(recipient_email=recipient_email,send_datetime=send_datetime,message_content=message_content)
        send_email(recipient_email, message_content, send_datetime)
        return redirect('home')
    else:
        return render(request, 'remember.html')


def view_all(request):
    events=Event.objects.all()
    return render(request, 'all.html', {'events':events})

    

