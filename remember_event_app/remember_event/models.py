from django.db import models

# Create your models here.

class Event(models.Model):
    recipient_email=models.EmailField()
    send_datetime=models.DateTimeField()
    message_content=models.TextField()

    def __str__(self):
        return self.recipient_email