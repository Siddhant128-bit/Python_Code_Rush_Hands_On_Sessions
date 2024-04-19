from django.http import HttpResponse
from django.shortcuts import render

def encrypt(request):
    if request.method == 'POST':
        text = str(request.POST.get('text'))
        key = int(request.POST.get('key'))
        encrypted_text = ''
        for letter in text:
            if (letter.isupper()):
                encrypted_text += chr((ord(letter) + key - 65) % 26 + 65)
            elif (letter.islower()):
                encrypted_text += chr((ord(letter) + key - 97) % 26 + 97)
            else:
                encrypted_text += letter
        return render(request, 'display.html', {'encrypted_text': encrypted_text})
    else:
        return render(request, 'index.html')