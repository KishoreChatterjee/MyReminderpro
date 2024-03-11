from django.db import models

class Reminder(models.Model):
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    reminder_type = models.CharField(max_length=10, choices=[('SMS', 'SMS'), ('Email', 'Email')])

    def __str__(self):
        return f"{self.date} {self.time} - {self.message} ({self.reminder_type})"
