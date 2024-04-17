from django.shortcuts import render,redirect
from django.http import HttpResponse
import json

def home(request):
    return render(request, "home.html")

def add(request):
    if request.method == "POST":
        added_note = request.POST.get('noteInput')

        try:
            with open("todo_list.json", "r") as file_variable:
                data = json.load(file_variable)
        except FileNotFoundError:
            data = []

        data.append(added_note)

        with open("todo_list.json", "w") as file_variable:
            json.dump(data, file_variable)

        return redirect('view')
    return render(request, 'add.html')


def view(request):
    # Read data from the todo_list.json file
    with open("todo_list.json", "r") as file_variable:
        data = json.load(file_variable)
        print("Content read from todo_list.json:", data)  # Debugging print statement

    return render(request, "view.html", {'added_note': data})