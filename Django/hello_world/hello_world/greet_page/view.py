from django.http import HttpResponse
import datetime

def greet_me(request):
    return HttpResponse('Hello World !!')

def greet_me_extra(request):
    #check time 
    #based on time 
    #display morning, afternoon,evening
    
    pass

def greet_me_again(request):
    return HttpResponse('somethinng or another')
