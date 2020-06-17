from django.db import models

# Create your models here.
class StaffAccount(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    job_code = models.IntegerField()
    job_title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.lname


class StaffAuth(models.Model):
    username = models.CharField(null=True, max_length=100)
    password = models.CharField(null=True, max_length=100)
    staff_id = models.ForeignKey(StaffAccount, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.username