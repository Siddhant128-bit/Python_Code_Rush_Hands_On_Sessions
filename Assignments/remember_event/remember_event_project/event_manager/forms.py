from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['recipient_email', 'scheduled_datetime', 'message_content']
