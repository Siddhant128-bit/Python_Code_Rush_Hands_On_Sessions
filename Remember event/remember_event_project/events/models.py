# events/models.py
from django.db import models

class Event(models.Model):
    recipient_email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    message_content = models.TextField()

    def __str__(self):
        return self.recipient_email
