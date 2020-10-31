from django.db import models
from studentauth.models import StudentAuth
from program.models import SchoolProgram

# Create your models here.

class StudentData(models.Model):
    fname = models.CharField(null=True, max_length=50)
    lname = models.CharField(null=True, max_length=50)
    email = models.CharField(null=True, max_length=100)
    student_number = models.CharField(null=True, max_length=15)
    phone_number = models.CharField(null=True, max_length=10)
    program_year = models.IntegerField(default=1)
    als = models.BooleanField(default=False)
    coop = models.BooleanField(default=False)
    international = models.BooleanField(default=False)
    program_id = models.ForeignKey(SchoolProgram, on_delete=models.CASCADE, default=1)
    auth_id = models.ForeignKey(StudentAuth, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.lname