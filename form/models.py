from django.db import models

# Create your models here.

class CareerCounselorForm(models.Model):
    q1_sso = models.BooleanField(default=False)
    q1_friend = models.BooleanField(default=False)
    q1_faculty = models.BooleanField(default=False)
    q1_visit = models.BooleanField(default=False)
    q1_orient = models.BooleanField(default=False)
    q1_event = models.BooleanField(default=False)
    q1_kpi = models.BooleanField(default=False)
    q1_outreach = models.BooleanField(default=False)
    q1_posters = models.BooleanField(default=False)
    q1_stv = models.BooleanField(default=False)
    q1_social = models.BooleanField(default=False)
    q1_media = models.BooleanField(default=False)
    ccs_resume = models.BooleanField(default=False)
    ccs_cover = models.BooleanField(default=False)
    ccs_interview = models.BooleanField(default=False)
    ccs_jobsearch = models.BooleanField(default=False)
    ccs_mockinterview = models.BooleanField(default=False)
    ccs_networking = models.BooleanField(default=False)
    ccs_portfolio = models.BooleanField(default=False)

    def __str__(self):
        return self.q1_sso

class EmploymentConsultantForm(models.Model):
    q1_sso = models.BooleanField(default=False)
    q1_friend = models.BooleanField(default=False)
    q1_faculty = models.BooleanField(default=False)
    q1_visit = models.BooleanField(default=False)
    q1_orient = models.BooleanField(default=False)
    q1_event = models.BooleanField(default=False)
    q1_kpi = models.BooleanField(default=False)
    q1_outreach = models.BooleanField(default=False)
    q1_posters = models.BooleanField(default=False)
    q1_stv = models.BooleanField(default=False)
    q1_social = models.BooleanField(default=False)
    q1_media = models.BooleanField(default=False)
    ccs_resume = models.BooleanField(default=False)
    ccs_cover = models.BooleanField(default=False)
    ecs_exploration = models.BooleanField(default=False)
    ecs_eplanning = models.BooleanField(default=False)
    ecs_cplanning = models.BooleanField(default=False)
    ecs_labourmarket = models.BooleanField(default=False)
    ecs_other = models.CharField(null=True, max_length=255)

    def __str__(self):
        return self.q1_sso

