from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.http import HttpResponse,HttpRequest

def home(request:HttpRequest)->HttpResponse:
    username=request.user.username if request.user.is_authenticated else None
    return render(request,'login_auth/home.html',{'username':username})

def signup_view(request:HttpRequest)->HttpResponse:
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()   
    return render(request,'login_auth/signup.html',{'form':form})

def login_view(request:HttpRequest)->HttpResponse:
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        form=AuthenticationForm()
    return render(request,'login_auth/login.html',{'form':form})

def logout_view(request:HttpRequest)->HttpResponse:
    logout(request)
    return redirect('login')