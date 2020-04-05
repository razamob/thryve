from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)
    student_number = models.CharField(max_length=15)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    program = models.CharField(max_length=250)
    program_year = models.IntegerField(default=1)

    def __str__(self):
        return self.name
