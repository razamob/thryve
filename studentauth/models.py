from django.db import models

# Create your models here.

#if we add natural key handling to Person, the fixture becomes much more humane. To add natural key handling, you 
 # define a default Manager for Person with a get_by_natural_key() method. In the case of a Person, a good natural 
 # key might be the pair:
 #(Deserialization of natural keys)Now Appointment can use that natural key to refer to StudentAccount objects
 #refer to https://docs.djangoproject.com/en/dev/topics/serialization/
class StudentAuthManager(models.Manager):                          #removed the neccessary feild from here  if u get the error "TypeError: Object of type SchoolProgram is not JSON serializable". remove it in other places below too cus thats more immediate
    def get_by_natural_key(self, sheridan_id, password):
        return self.get(sheridan_id=sheridan_id, password=password)



class StudentAuth(models.Model):
    sheridan_id = models.CharField(null=True, max_length=10)
    password = models.CharField(null=True, max_length=100)
    
    #define a default Manager for StudentAuth
    objects = StudentAuthManager()

    #metadata is “anything that’s not a field
    class Meta:                   #removed the neccessary feild from here  if u get the error "TypeError: Object of type SchoolProgram is not JSON serializable". remove it in other places below too cus thats more immediate 
        #this is what is actually group in the serialized object's feild column for the specific feild foreighn key attribute
        #Sets of field names that, taken together, must be unique:
        #unique_together can be a single list when dealing with a single set of fields:
        unique_together = ['sheridan_id', 'password']

    #This method should always return a natural key tuple 
    #Then, when you call serializers.serialize(), you provide use_natural_foreign_keys=True or use_natural_primary_keys=True arguments
    def natural_key(self):              #removed the neccessary feild from here  if u get the error "TypeError: Object of type SchoolProgram is not JSON serializable". remove it in other places below too cus thats more immediate
        #made this dictionary return whitch will add to the previous dictionary
        return {'sheridan_id':self.sheridan_id,'password': self.password}




    def __str__(self):
        return self.sheridan_id