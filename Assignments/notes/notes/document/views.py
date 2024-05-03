from django.shortcuts import render
from .models import Note
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout

@login_required(login_url='/login/')
def editor(request):
    docid= int(request.GET.get('docid',0))
    notes= Note.objects.all()

    if request.method == 'POST':
        docid = int(request.POST.get('docid',0))
        title = request.POST.get('title')
        content = request.POST.get('content','')

        if docid>0:
            notes = Note.objects.get(pk=docid)
