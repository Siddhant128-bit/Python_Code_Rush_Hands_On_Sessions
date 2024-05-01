from django.http import HttpResponse

def say_bye(request):
    return HttpResponse("Hello, I am bye page")