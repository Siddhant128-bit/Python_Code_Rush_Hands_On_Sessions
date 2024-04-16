import json
from django.shortcuts import render

def view(request):
    # Load existing notes from the JSON file
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []

    # Pass the notes data to the template
    context = {'notes': notes}
    
    return render(request, 'view.html', context)
