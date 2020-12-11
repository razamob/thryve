from django.db import models

# Create your models here.
class SchoolProgram(models.Model):
    program_code = models.CharField(max_length=6)
    program_title = models.CharField(max_length=100)
    faculty_code = models.CharField(max_length=5)
    educ_level = models.CharField(max_length=5)

    #This method should always return a natural key tuple 
    #Then, when you call serializers.serialize(), you provide use_natural_foreign_keys=True or use_natural_primary_keys=True arguments
    def natural_key(self):              #removed the neccessary feild from here  if u get the error "TypeError: Object of type SchoolProgram is not JSON serializable". remove it in other places below too cus thats more immediate
        #made this dictionary return whitch will add to the previous dictionary
        return {'program_code':self.program_code,'program_title': self.program_title, 'faculty_code': self.faculty_code, 'educ_level': self.educ_level}


    def __str__(self):
        return self.program_title