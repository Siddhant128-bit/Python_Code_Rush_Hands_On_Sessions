from django.shortcuts import render
from django.http import HttpResponse
import string

ENCRYPT_HOME_TEMPLATE = 'encrypt_text/home.html'

def caesar_cipher_encrypt(text, key):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) + key - 65) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) + key - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, key):
    decrypted_text = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr((ord(char) - key - 65) % 26 + 65)
            else:
                decrypted_text += chr((ord(char) - key - 97) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text

def home(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        key = int(request.POST.get('key'))
        operation = request.POST.get('operation')
        
        if operation == 'encrypt':
            result = caesar_cipher_encrypt(text, key)
            return render(request, ENCRYPT_HOME_TEMPLATE, {'result': result, 'operation': 'Encrypted'})
        elif operation == 'decrypt':
            result = caesar_cipher_decrypt(text, key)
            return render(request, ENCRYPT_HOME_TEMPLATE, {'result': result, 'operation': 'Decrypted'})
    return render(request, ENCRYPT_HOME_TEMPLATE)
