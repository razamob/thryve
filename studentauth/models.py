from django.db import models

# Create your models here.

class StudentAuth(models.Model):
    sheridan_id = models.CharField(null=True, max_length=10)
    password = models.CharField(null=True, max_length=100)
    
    def __str__(self):
        return self.sheridan_id