from django.http import HttpResponse
import datetime

def greet_me(request):
    return HttpResponse("Hello, Django!")

def greet_using_time(request):
    current_time = datetime.datetime.now().time()
    if current_time.hour < 12:
        greeting = "Good morning!"
    elif 12 <= current_time.hour < 18:
        greeting = "Good afternoon!"
    else:
        greeting = "Good evening!"
    return HttpResponse(greeting)