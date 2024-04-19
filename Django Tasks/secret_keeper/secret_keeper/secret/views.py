from django.shortcuts import render

def caesar_cipher(text, key, decrypt=False):
    # Performs Caesar Cipher encryption or decryption
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # Shift text to right for encryption and to left for decryption
    # Concatenate char at index key till the end and chars from beginning till key(excluding)
    shifted_alphabet = alphabet[key:] + alphabet[:key]
    if decrypt:
        shifted_alphabet = alphabet[-key:] + alphabet[:-key]
    result = ''
    # Loop over each char
    for char in text:
        if char.isalpha():
            # Find index of current char in alphabet
            index = alphabet.index(char.lower())
            # Retreive corresponding shifted char
            shifted_char = shifted_alphabet[index] if char.islower() else shifted_alphabet[index].upper()
            result += shifted_char
        else:
            result += char
    return result

def home(request):
    output = ''
    if request.method == 'POST':
        text = request.POST.get('mainText', '')
        
        try:
            key = int(request.POST.get('key', 0))
        except ValueError:
            return render(request, 'index.html', {'error_msg': 'Key must be an integer!!'})
        
        mode = request.POST.get('mode', '')
        if mode == 'encrypt':
            output = caesar_cipher(text, key)
        elif mode == 'decrypt':
            output = caesar_cipher(text, key, decrypt=True)
        else:
            output = "Invalid mode selected"
        return render(request, 'output.html', {'output': output})

    return render(request, 'index.html')
