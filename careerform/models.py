from django.db import models

# Create your models here.

class CareerCounselorForm(models.Model):
    q1c_sso = models.BooleanField(default=False)
    q1c_friend = models.BooleanField(default=False)
    q1c_faculty = models.BooleanField(default=False)
    q1c_visit = models.BooleanField(default=False)
    q1c_orient = models.BooleanField(default=False)
    q1c_event = models.BooleanField(default=False)
    q1c_kpi = models.BooleanField(default=False)
    q1c_outreach = models.BooleanField(default=False)
    q1c_posters = models.BooleanField(default=False)
    q1c_stv = models.BooleanField(default=False)
    q1c_social = models.BooleanField(default=False)
    q1c_media = models.BooleanField(default=False)
    q1c_walkby = models.BooleanField(default=False)
    q1c_website = models.BooleanField(default=False)
    ccs_exploration = models.BooleanField(default=False)
    ccs_eplanning = models.BooleanField(default=False)
    ccs_cplanning = models.BooleanField(default=False)
    ccs_labourmarket = models.BooleanField(default=False)
    ccs_other = models.BooleanField(default=False)

    #metadata is “anything that’s not a field
    #class Meta:                   #im removed program_id to see if that did anything to error "TypeError: Object of type SchoolProgram is not JSON serializable"
        #this is what is actually group in the serialized object's feild column for the specific feild foreighn key attribute
        #Sets of field names that, taken together, must be unique:
        #unique_together can be a single list when dealing with a single set of fields:
    #    unique_together = ['q1c_sso', 'q1c_friend', 'q1c_faculty', 'q1c_visit', 'q1c_orient', 'q1c_event', 'q1c_kpi', 'q1c_outreach', 'q1c_posters', 'q1c_stv', 'q1c_social', 'q1c_media', 'q1c_walkby', 'q1c_website', 'ccs_exploration', 'ccs_eplanning', 'ccs_cplanning', 'ccs_labourmarket', 'ccs_other']
        
    #This method should always return a natural key tuple 
    #Then, when you call serializers.serialize(), you provide use_natural_foreign_keys=True or use_natural_primary_keys=True arguments
    def natural_key(self):             #im removed program_id to see if that did anything to error "TypeError: Object of type SchoolProgram is not JSON serializable"
        #made this dictionary return whitch will add to the previous dictionary
        return {'q1c_sso':self.q1c_sso, 'q1c_friend':self.q1c_friend, 'q1c_faculty':self.q1c_faculty, 'q1c_visit': self.q1c_visit, 'q1c_orient':self.q1c_orient, 'q1c_event':self.q1c_event, 'q1c_kpi':self.q1c_kpi, 'q1c_outreach':self.q1c_outreach, 'q1c_posters':self.q1c_posters, 'q1c_stv':self.q1c_stv, 'q1c_social':self.q1c_social, 'q1c_media':self.q1c_media, 'q1c_walkby':self.q1c_walkby, 'q1c_website':self.q1c_website, 'ccs_exploration':self.ccs_exploration, 'ccs_eplanning':self.ccs_eplanning, 'ccs_cplanning':self.ccs_cplanning, 'ccs_labourmarket':self.ccs_labourmarket, 'ccs_other':self.ccs_other}
        #i can change the return for this to the below code if i choose to limit the displayed feilds
        #return {'q1c_sso':self.q1c_sso, 'q1c_friend':self.q1c_friend}

    def __str__(self):
        return self.q1c_event