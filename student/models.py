from django.db import models
from program.models import SchoolProgram

# Create your models here.
class StudentAccount(models.Model):
    fname = models.CharField(null=True, max_length=50)
    lname = models.CharField(null=True, max_length=50)
    email = models.CharField(null=True, max_length=100)
    student_number = models.CharField(null=True, max_length=15)
    phone = models.ForeignKey(SchoolProgram, on_delete=models.CASCADE, null=True)
    program_year = models.IntegerField(default=1)
    als = models.BooleanField(default=False)
    coop = models.BooleanField(default=False)
    international = models.BooleanField(default=False)
    
    def __str__(self):
        return self.lname

class StudentAuth(models.Model):
    sheridan_id = models.CharField(null=True, max_length=10)
    password = models.CharField(null=True, max_length=100)
    student_id = models.ForeignKey(StudentAccount, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.sheridan_id
