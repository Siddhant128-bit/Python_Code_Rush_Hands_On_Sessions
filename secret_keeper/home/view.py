from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    if request.method == 'POST':
        plain_text = request.POST.get('plain_text')
        key = int(request.POST.get('key'))
        if plain_text:
            encrypted_text = caesar_cipher_encrypt(plain_text, key)
            return render(request, 'display.html', {'result': encrypted_text})

    return render(request, 'home.html')


def caesar_cipher_encrypt(plain_text, key):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            shifted = ord(char) + key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text
