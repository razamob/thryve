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
    ecs_resume = models.BooleanField(default=True)
    ecs_cover = models.BooleanField(default=True)
    ecs_interview = models.BooleanField(default=True)
    ecs_jobsearch = models.BooleanField(default=True)
    ecs_mockinterview = models.BooleanField(default=True)
    ecs_networking = models.BooleanField(default=True)
    ecs_portfolio = models.BooleanField(default=True)

    #metadata is “anything that’s not a field
    class Meta:                   #im removed program_id to see if that did anything to error "TypeError: Object of type SchoolProgram is not JSON serializable"
        #this is what is actually group in the serialized object's feild column for the specific feild foreighn key attribute
        #Sets of field names that, taken together, must be unique:
        #unique_together can be a single list when dealing with a single set of fields:
        unique_together = [['q1e_sso', 'q1e_friend', 'q1e_faculty', 'q1e_visit', 'q1e_orient', 'q1e_event', 'q1e_kpi2', 'q1e_outreach', 'q1e_posters', 'q1e_stv', 'q1e_social', 'q1e_media', 'q1e_walkby', 'q1e_website', 'ecs_resume', 'ecs_cover', 'ecs_interview', 'ecs_jobsearch', 'ecs_mockinterview', 'ecs_networking', 'ecs_portfolio']]

    #This method should always return a natural key tuple 
    #Then, when you call serializers.serialize(), you provide use_natural_foreign_keys=True or use_natural_primary_keys=True arguments
    def natural_key(self):             #im removed program_id to see if that did anything to error "TypeError: Object of type SchoolProgram is not JSON serializable"
        #made this dictionary return whitch will add to the previous dictionary
        return {'q1e_sso':self.q1e_sso, 'q1e_friend':self.q1e_friend, 'q1e_faculty':self.q1e_faculty, 'q1e_visit':self.q1e_visit, 'q1e_orient':self.q1e_orient, 'q1e_event':self.q1e_event, 'q1e_kpi2':self.q1e_kpi2, 'q1e_outreach':self.q1e_outreach, 'q1e_posters':self.q1e_posters, 'q1e_stv':self.q1e_stv, 'q1e_social':self.q1e_social, 'q1e_media':self.q1e_media, 'q1e_walkby':self.q1e_walkby, 'q1e_website':self.q1e_website, 'ecs_resume':self.ecs_resume, 'ecs_cover':self.ecs_cover, 'ecs_interview':self.ecs_interview, 'ecs_jobsearch':self.ecs_jobsearch, 'ecs_mockinterview':self.ecs_mockinterview, 'ecs_networking':self.ecs_networking, 'ecs_portfolio':self.ecs_portfolio}






    def __str__(self):
        return self.q1e_event
