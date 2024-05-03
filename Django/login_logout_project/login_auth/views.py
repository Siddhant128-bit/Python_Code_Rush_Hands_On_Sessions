# login_auth/views.py

from django.shortcuts import render, redirect

#important imports ########################## 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
###############################

from django.http import HttpRequest
from django.http import HttpResponse

def home_view(request: HttpRequest) -> HttpResponse:
    """
    View function for the home page.
    
    Retrieves the username of the logged-in user and renders the home template.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: The HTTP response object containing the rendered home template.
    """
    username = request.user.username if request.user.is_authenticated else None
    return render(request, 'login_auth/home.html', {'username': username})


def signup_view(request: HttpRequest) -> HttpResponse:
    """
    View function for the signup page.
    
    Handles user registration and renders the signup template.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: The HTTP response object containing the rendered signup template.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'login_auth/signup.html', {'form': form})



def login_view(request: HttpRequest) -> HttpResponse:
    """
    View function for the login page.
    
    Handles user authentication and redirects to the home page upon successful login.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: The HTTP response object containing the rendered login template.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login_auth/login.html', {'form': form})

def logout_view(request: HttpRequest) -> HttpResponse:
    """
    View function for the logout functionality.
    
    Logs out the current user and redirects to the login page.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: The HTTP response object containing the redirect to the login page.
    """
    logout(request)
    return redirect('login')
