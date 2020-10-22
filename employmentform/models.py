from django.db import models

# Create your models here.
class EmploymentConsultantForm(models.Model):
    q1e_sso = models.BooleanField(default=False)
    q1e_friend = models.BooleanField(default=False)
    q1e_faculty = models.BooleanField(default=False)
    q1e_visit = models.BooleanField(default=False)
    q1e_orient = models.BooleanField(default=False)
    q1e_event = models.BooleanField(default=False)
    q1e_kpi2 = models.BooleanField(default=False)
    q1e_outreach = models.BooleanField(default=False)
    q1e_posters = models.BooleanField(default=False)
    q1e_stv = models.BooleanField(default=False)
    q1e_social = models.BooleanField(default=False)
    q1e_media = models.BooleanField(default=False)
    q1e_walkby = models.BooleanField(default=False)
    q1e_website = models.BooleanField(default=False)
    ecs_exploration = models.BooleanField(default=False)
    ecs_eplanning = models.BooleanField(default=False)
    ecs_cplanning = models.BooleanField(default=False)
    ecs_labourmarket = models.BooleanField(default=False)
    ecs_other = models.BooleanField(default=False)

    def __str__(self):
        return self.title
