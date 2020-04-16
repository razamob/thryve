from django.db import models
from students.models import Student


class Appointment(models.Model):
    title = models.CharField(max_length=300, null=True)
    start_date = models.DateTimeField(null=True, blank=False)
    end_date = models.DateTimeField(null=True, blank=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
