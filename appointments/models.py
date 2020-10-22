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
    student_id = models.ForeignKey(StudentAccount, on_delete=models.CASCADE, null=True)
    staff_id = models.ForeignKey(StaffAccount, on_delete=models.CASCADE, null=True)
    cc_form = models.ForeignKey(CareerCounselorForm, on_delete=models.CASCADE, null=True)
    ec_form = models.ForeignKey(EmploymentConsultantForm, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
