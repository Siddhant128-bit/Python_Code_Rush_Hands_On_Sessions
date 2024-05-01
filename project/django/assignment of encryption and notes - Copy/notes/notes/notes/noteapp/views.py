from django.shortcuts import render
import json
import os
from datetime import datetime  


# Path to the JSON file to store notes
NOTES_FILE = os.path.join(os.path.dirname(__file__), 'notes.json')

def save_notes(notes_data):
    with open(NOTES_FILE, 'w') as f:
        json.dump(notes_data, f)

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r') as f:
            return json.load(f)
    return []

def add_note(request):
    if request.method == 'POST':
        note_text = request.POST.get('note', '')
        if note_text:
            notes_data = load_notes()
            notes_data.append({'text': note_text, 'date': str(datetime.now())})
            save_notes(notes_data)
    return render(request, 'add_note.html')

def view_notes(request):
    notes_data = load_notes()
    return render(request, 'view_notes.html', {'notes': notes_data})
