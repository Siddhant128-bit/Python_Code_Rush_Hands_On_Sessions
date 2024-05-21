from django.shortcuts import render
from .utils import caesar_cipher

def home(request):
    return render(request, 'secret_keeper/home.html')

def encrypt(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        key = int(request.POST.get('key', ''))
        encrypted_text = caesar_cipher(text, key)
        return render(request, 'secret_keeper/result.html', {'encrypted_text': encrypted_text})
    return render(request, 'secret_keeper/home.html')

