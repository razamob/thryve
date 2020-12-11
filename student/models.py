from django.db import models
from studentauth.models import StudentAuth
from program.models import SchoolProgram

# Create your models here.

# if we add natural key handling to Person, the fixture becomes much more humane. To add natural key handling, you
# define a default Manager for Person with a get_by_natural_key() method. In the case of a Person, a good natural
# key might be the pair:
# (Deserialization of natural keys)Now Appointment can use that natural key to refer to StudentAccount objects
# refer to https://docs.djangoproject.com/en/dev/topics/serialization/


# im removed program_id to see if that did anything to error "TypeError: Object of type SchoolProgram is not JSON serializable"
class StudentAccountManager(models.Manager):
    def get_by_natural_key(self, fname, lname, email, student_number, phone_number, program_year, als, coop, international, auth_id):
        return self.get(fname=fname, lname=lname, email=email, student_number=student_number, phone_number=phone_number, program_year=program_year, als=als, coop=coop, international=international, auth_id=auth_id)


class StudentAccount(models.Model):
    education_level = models.CharField(null=True, max_length=50)
    gpa = models.CharField(null=True, max_length=5)
    program_year = models.CharField(null=True, max_length=2)
    als = models.BooleanField(null=True)
    coop = models.BooleanField(null=True)
    international = models.BooleanField(null=True)
    fname = models.CharField(null=True, max_length=50)
    lname = models.CharField(null=True, max_length=50)
    email = models.CharField(null=True, max_length=100)
    student_number = models.CharField(null=True, max_length=15)
    phone_number = models.CharField(null=True, max_length=10)
    student_status = models.CharField(null=True, max_length=4)
    program_id = models.ForeignKey(SchoolProgram, on_delete=models.CASCADE, null=True)
    auth_id = models.ForeignKey(StudentAuth, on_delete=models.CASCADE, null=True)

    # define a default Manager for StudentAccount
    objects = StudentAccountManager()

    # metadata is “anything that’s not a field
    # class Meta:                   #im removed program_id to see if that did anything to error "TypeError: Object of type SchoolProgram is not JSON serializable"
    # this is what is actually group in the serialized object's feild column for the specific feild foreighn key attribute
    # Sets of field names that, taken together, must be unique:
    # unique_together can be a single list when dealing with a single set of fields:
    #unique_together = [['fname', 'lname', 'email', 'student_number', 'phone_number', 'program_year', 'als', 'coop', 'international', 'auth_id']]

    # This method should always return a natural key tuple
    # Then, when you call serializers.serialize(), you provide use_natural_foreign_keys=True or use_natural_primary_keys=True arguments
    def natural_key(self):  # im removed program_id to see if that did anything to error "TypeError: Object of type SchoolProgram is not JSON serializable"
        # made this dictionary return whitch will add to the previous dictionary
        return {'fname': self.fname, 'lname': self.lname, 'email': self.email, 'student_number': self.student_number, 'phone_number': self.phone_number, 'program_year': self.program_year, 'als': self.als, 'coop': self.coop, 'international': self.international, 'auth_id': self.auth_id.natural_key(), 'program_id': self.program_id.natural_key(), 'student_status': self.student_status}
    # This definition ensures that all StudentAuth objects are serialized before any StudentAccount objects. In turn,
    # any object referencing StudentAccount will be serialized after both StudentAuth and StudentAccount have been serialized.
    # THIS MIGHT AFFECT THE OTHER SERIALIZATIONS THAT MY TEAM MEMBERS DID BTW SOO CHECK WITH EM
    # THE SECOND ONE(FOREIGHN KEY DEEPER WITHIN APPOINTMENT) CALLED SEEMS TO BE ADDED AS APART OF THIS LIST!!!!
    natural_key.dependencies = ['studentauth.studentAuth','program.schoolProgram']

    def __str__(self):
        return self.lname
