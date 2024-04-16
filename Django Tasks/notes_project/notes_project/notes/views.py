from django.shortcuts import render, redirect
import json
import os
from datetime import datetime

def add_note(request):
    if request.method == 'POST':
        note_content = request.POST.get('note_content')
        save_note(note_content)
        return redirect('view_notes') 
    return render(request, 'add_note.html')

def view_notes(request):
    notes = load_notes()
    return render(request, 'view_notes.html', {'notes': notes})

def save_note(note_content):
    notes_file = os.path.join(os.path.dirname(__file__), 'notes.json')
    current_time = datetime.now().strftime("%Y-%m-%d")
    if os.path.exists(notes_file):
        with open(notes_file, 'r') as f:
            notes = json.load(f)
    else:
        notes = []

    notes.append({'content': note_content, 'date': current_time})


    with open(notes_file, 'w') as f:
        json.dump(notes, f)

def load_notes():
    notes_file = os.path.join(os.path.dirname(__file__), 'notes.json')
    if not os.path.exists(notes_file):
        return []
    with open(notes_file, 'r') as f:
        return json.load(f)