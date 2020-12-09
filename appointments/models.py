from django.db import models
from students.models import Student
from student.models import StudentAccount
from staff.models import StaffAccount
from employmentform.models import EmploymentConsultantForm
from careerform.models import CareerCounselorForm

class Appointment(models.Model):
    title = models.CharField(max_length=300, null=True)
    start_date = models.DateTimeField(null=True, blank=False)
    end_date = models.DateTimeField(null=True, blank=False)
    submission_date = models.DateTimeField(null=True, blank=False)
    approval_date = models.DateTimeField(null=True, blank=False)
    description = models.TextField(null=True, blank=True)
    student_notes = models.CharField(max_length=300, null=True)
    staff_notes = models.CharField(max_length=300, null=True)
    attachment1 = models.CharField(max_length=300, null=True)
    attachment2 = models.CharField(max_length=300, null=True)
    attachment3 = models.CharField(max_length=300, null=True)
    status = models.CharField(max_length=20, null=True)
    delete_appointment_row = models.BooleanField(default=False, null=True, blank=True)
    student_id = models.ForeignKey(StudentAccount, on_delete=models.CASCADE, null=True)
    staff_id = models.ForeignKey(StaffAccount, on_delete=models.CASCADE, null=True)
    cc_form = models.ForeignKey(CareerCounselorForm, on_delete=models.CASCADE, null=True)
    ec_form = models.ForeignKey(EmploymentConsultantForm, on_delete=models.CASCADE, null=True)

    # If your natural key refers to another object (by using a foreign key or natural key to another
    # object as part of a natural key), then you need to be able to ensure that the objects on which
    # a natural key depends occur in the serialized data before the natural key requires them.
    # To control this ordering, you can define dependencies on your natural_key() methods.
    # You do this by setting a dependencies attribute on the natural_key() method itself.
    def natural_key(self):
        #This return is what determines the datatype(ex, tuple, list, dictionary) that the objects foreighkey holds at currently "student_id"
        #As it is right now it's dictionary by default, you can add a anoth dictionary to a dictionary so that is what we did here, commas can change outcomes
        return (self.title, self.start_date, self.end_date, self.submission_date, self.approval_date, self.description, self.student_notes, self.staff_notes, self.attachment1, self.attachment2, self.attachment3, self.status, self.delete_appointment_row, self.staff_id, self.cc_form, self.ec_form) + self.student_id.natural_key()
    #This definition ensures that all StudentAccount objects are serialized before any Appointment objects. In turn, 
    # any object referencing Appointment will be serialized after both StudentAccount and Appointment have been serialized.
    #THIS MIGHT AFFECT THE OTHER SERIALIZATIONS THAT MY TEAM MEMBERS DID BTW SOO CHECK WITH EM
    natural_key.dependencies = ['student.studentAccount', 'careerform.careerCounselorForm']
    #natural_key.dependencies = ['careerform.careerCounselorForm']

def __str__(self):
    return self.title
