from django.db import models

class Event(models.Model):
    recipient_email = models.EmailField()
    scheduled_datetime = models.DateTimeField()
    message_content = models.TextField()

    def __str__(self):
        return f"{self.recipient_email} - {self.scheduled_datetime}" 



