from django.shortcuts import render

def notes(request):
    return render(request,'homepage.html')
