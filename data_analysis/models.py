from django.db import models

# Create your models here.


class School(models.Model):
    id = models.IntegerField(default=1, primary_key=True)
    program_year = models.IntegerField(default=1)
    program_type = models.CharField(max_length=70)
    grade = models.DecimalField(max_digits=5, decimal_places=2)
    co_op = models.BooleanField()
    international = models.BooleanField()
