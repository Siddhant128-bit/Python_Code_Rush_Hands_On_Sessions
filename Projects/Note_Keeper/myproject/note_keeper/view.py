import json
from django.shortcuts import render

def view(request):
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []

    context = {'notes': notes}
    
    return render(request, 'view.html', context)
