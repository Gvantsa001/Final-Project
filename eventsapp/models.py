from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    event_manager = models.ForeignKey(EventManager, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=200)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title