import json
from datetime import datetime
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  
def add(request):
    if request.method == 'POST':
        note_message = request.POST.get('note_message')
        
        # Get the current date and time
        current_datetime = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

        # Load existing notes from the JSON file
        try:
            with open('notes.json', 'r') as file:
                notes = json.load(file)
        except FileNotFoundError:
            notes = []

        # Add the new note message and its timestamp to the list of notes
        notes.append({'message': note_message, 'timestamp': current_datetime})

        # Write the updated notes list back to the JSON file
        with open('notes.json', 'w') as file:
            json.dump(notes, file)

        # Redirect to the notes page
        return redirect('notes')

    return render(request, 'add.html')
