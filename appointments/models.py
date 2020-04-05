from django.db import models
from students.models import Student


class Appointment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=300)
    start_date = models.DateTimeField(blank=False)
    end_date = models.DateTimeField(blank=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
