from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render, redirect

def caesar_cipher(text, key, decrypt=False):
    result = ''
    for char in text:
        if char.isalpha(): # Check if the character is an alphabet
            shift = ord('A' if char.isupper() else 'a') # Determine the shift based on uppercase or lowercase for capital  "A" is based on ascii value of A
            decrypted_char = chr((ord(char) - shift + (26 - key if decrypt else key)) % 26 + shift)
            result += decrypted_char # Non-alphabetic characters remain unchanged
        else:
            result += char
    return result

def home(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        key = int(request.POST.get('key', 0))
        mode = request.POST.get('mode', '')  # 'encrypt' or 'decrypt'
        if mode == 'encrypt':
            encrypted_text = caesar_cipher(text, key)
            return render(request, 'output.html', {'output': encrypted_text})
       
    return render(request, 'index.html')

def back(request):
    return redirect('home')
