from django.db import models

# Create your models here.
class SchoolProgram(models.Model):
    program_code = models.CharField(max_length=6)
    program_title = models.CharField(max_length=100)
    faculty_code = models.CharField(max_length=5)
    educ_level = models.CharField(max_length=5)

    def __str__(self):
        return self.program_title