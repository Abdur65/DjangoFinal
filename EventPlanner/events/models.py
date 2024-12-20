from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200)
    date_time = models.DateTimeField()
    capacity = models.IntegerField()
    
    status = {
            'upcoming': 'Upcoming',
            'ongoing': 'Ongoing',
            'completed': 'Completed',
    }
