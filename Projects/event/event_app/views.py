from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .models import ScheduledEvent

import smtplib
import ssl
import datetime as dt
import time

def remember_event(request):
    if request.method == 'POST':
        title = request.POST['title']
        email = request.POST['email']
        message = request.POST['message']
        scheduled_datetime_str = request.POST['scheduled_datetime']  
        
        scheduled_datetime = dt.datetime.strptime(scheduled_datetime_str, '%Y-%m-%dT%H:%M')
        
        ScheduledEvent.objects.create(
            title=title,
            email=email,
            message=message,
            scheduled_datetime=scheduled_datetime
        )
        
        context = ssl.create_default_context()
        with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
            server.starttls(context=context)
            server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            
            current_time = dt.datetime.now()
            time_difference = (scheduled_datetime - current_time).total_seconds()
            if time_difference > 0:
                time.sleep(time_difference)
            
            email_message = f"Subject: {title}\n\n{message}"
            
            server.sendmail(
                settings.EMAIL_HOST_USER,
                [email],
                email_message,
            )
            return render(request, 'home_page.html')

    return render(request, 'remember_event.html')

def home_page(request):
     return render(request, 'home_page.html')

def all_event(request):
    events=ScheduledEvent.objects.all()
    return render(request, 'all_event.html',{'events':events})
