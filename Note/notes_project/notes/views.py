# notes/views.py
from django.shortcuts import render
from django.http import JsonResponse
import json
from datetime import datetime

def add_notes(request):
    if request.method == 'POST':
        note_text = request.POST.get('note_text')
        if note_text:
            # Get current datetime
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Load existing notes from JSON file
            try:
                with open('notes.json', 'r') as file:
                    notes = json.load(file)
            except FileNotFoundError:
                notes = []

            # Append new note to the list
            notes.append({'text': note_text, 'date': current_datetime})

            # Write updated notes to JSON file
            with open('notes.json', 'w') as file:
                json.dump(notes, file, indent=4)

    return render(request, 'add_notes.html')

def view_notes(request):
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []

    return render(request, 'view_notes.html', {'notes': notes})

