from django.db import models

class ScheduledEvent(models.Model):
    email = models.EmailField()
    title = models.CharField(max_length=100)
    message = models.TextField()
    scheduled_datetime = models.DateTimeField()


    def __str__(self):
        return self.title
