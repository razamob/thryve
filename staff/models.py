from django.db import models

# Create your models here.


class StaffAuth(models.Model):
    username = models.CharField(null=True, max_length=100)
    password = models.CharField(null=True, max_length=100)

    def __str__(self):
        return self.username


class StaffAccount(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    job_code = models.IntegerField()
    job_title = models.CharField(max_length=50)
    auth_id = models.ForeignKey(StaffAuth, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.lname
