from django.db import models


from django import forms

# Create your models here.

class CareerForm(models.Model):
    sso = models.BooleanField(default=False)

    def __str__(self):
        return self.q1_sso

class EmploymentForm(models.Model):
    sso = models.BooleanField(default=False)

    def __str__(self):
        return self.q1_sso

class DateInput(forms.DateInput):
    input_type = 'datetime-local'

class CheckFrequencyForm(forms.Form):
    #name = forms.CharField(max_length=200)
    #student_number = forms.CharField(max_length=15)
    #start_date = forms.DateTimeField(blank=False)
    #end_date = forms.DateTimeField(blank=False)

    # they will all be text input unless i change the widget
    #change defaults
    name = forms.CharField(max_length=200, label='Student Name', required=False, widget=forms.TextInput(attrs={"class":"form-control"})) #"class":"form-control",
    # because of this minimum length an error can pop up for me if user puts in a student number over 15
    # shouldn't the student bumber be integer feild?
    #student_number = forms.CharField(max_length=15, required=False,widget=forms.NumberInput(attrs={'size': '20'}))
    student_number = forms.IntegerField(label='Student Number', required=False, widget=forms.NumberInput(attrs={"class":"form-control"})) #"placeholder": 33

    start_date = forms.DateTimeField(label='Start Date', widget=DateInput(attrs={"class":"form-control"}))
    end_date = forms.DateTimeField(label='End Date', widget=DateInput(attrs={"class":"form-control"}))
    

    # the individual clean_... check methods run first in sequenqial order then it goes to the clean(), 
    # the fields you are wanting to validate might not have survived the initial individual field checks
    '''
    # it has to use these kinda naming structure for validating
    def clean_name(self):
        # i have to return the input feild type in this feild variable input type version of clean
        name = self.cleaned_data.get("name")
        student_number = self.cleaned_data.get("student_number")
        print(type(name))
        print(type(student_number))
        print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
        print("I have name: ", name, " and student number :", student_number)
        print("the length of name is ",len(name))
        #if not empty
        #if less than 201 characters
        #EXAMPLE CODE: change this code below
        #if "iggy" in name:
        #    return name
        #else:
        #    raise forms.ValidationError("This is ")
        if name !="" or len(name)!= 0:# don't use "if name !=None" use instead "name !='' "
            print("1")
            if student_number != None:
                print("3")
                return name
            print("4")
            return name

        else:
            print("2")
            if student_number is not None:# use none for numbers
                print("5")
                return name
            else:
                print("6")
                #When this below validation is used both multiple validations that it refers to will just go over the 1 feild variable that this clean covers so know that
                #raise forms.ValidationError([forms.ValidationError("Must input a name here or fill out the student id feild in the number box beside this."),forms.ValidationError("Must input a student number here or fill out the name feild in the text box beside this.")])
                raise forms.ValidationError("Must input a name here or fill out the student id feild in the number box beside this.")
                return name
        


    
    def clean_student_number(self):
        # i have to return the input feild type in this feild variable input type version of clean
        student_number = self.cleaned_data.get("student_number")
        name = self.cleaned_data.get("name")
        print(type(name))
        print(type(student_number))
        #if not empty
        #if less than 16 characters 
        #EXAMPLE CODE: change this code below
        print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
        print("I have student number: ", student_number, " and name :", name)
        print("the length of student number is ",len(student_number))
        #print("the length of name is ",len(name))
        #if "iggy" in student_number:
        #    return name
        if student_number !="" or len(student_number)!= 0: # use none here
            print("1")
            
            if name !=None:
                print("3")
                return student_number
            print("4")
            return student_number

        else:
            print("2")
            if name !=None:
                print("5")
                return student_number
            else:
                print("6")
                raise forms.ValidationError("Must input a student number here or fill out the name feild in the text box beside this.")
                #When this below validation is used both multiple validations that it refers to will just go over the 1 feild variable that this clean covers so know that
                #raise forms.ValidationError([forms.ValidationError("Must input a name here or fill out the student id feild in the number box beside this."),forms.ValidationError("Must input a student number here or fill out the name feild in the text box beside this.")])
                # dont forget to return or you might see problems with validation
                return student_number
    
    
  '''  
    def clean(self):
        # i don't have to return the input feild type in clean()
        cleaned_data = super(CheckFrequencyForm, self).clean()
        name = self.cleaned_data.get("name")
        student_number = self.cleaned_data.get("student_number")


        error_dict = {}

        start_date = self.cleaned_data.get("start_date")
        end_date = self.cleaned_data.get("end_date")
        # Must use type() on the input feild so you know what type you are working with, each input type has their own corresponding variable type 
        print(type(name))
        print(type(student_number))
        print(type(start_date))
        print(type(end_date))
        #if not empty
        #if less than 16 characters 
        #EXAMPLE CODE: change this code below
        print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
        print("I have student number: ", student_number, " and name :", name)
        #The len() function returns the number of items in an object.An object. Must be a sequence or a collection
        #so using len() on a integer will give us errors
        print("the length of str(student_number) is ",len(str(student_number)))
        print("the actual value of student_number is ",student_number)
        print("the length of name is ",len(name))


        if name !="" or len(name)!= 0:# don't use "if name !=None" use instead "name !='' "
            print("1")
            #student_number is not None
            #if (str(student_number) != "" or len(str(student_number)) != 0):
            # i wonder if if(student_number !=None): will work also?
            #if (student_number is not None):
            if(student_number !=None):
                print("3")
                
            print("4")
            

        else:
            print("2")
            #if str(student_number) != "" or len(str(student_number))!= 0:
            #if (student_number is not None):
            if(student_number !=None):
                print("5")
                
            else:
                print("6")
                # the dict key value name must be the actual feild name or you will get an error!!

                # this also works for making the validation show up on top of the different and separate form inputs, whitch are within the from
                '''
                #error_dict = {}
                error_dict['name'] = forms.ValidationError("Must input a name here or fill out the student id feild in the number box beside this.")
                error_dict['student_number'] = forms.ValidationError("Must input a student number here or fill out the name feild in the text box beside this.")
                raise forms.ValidationError(error_dict)
                '''
                # this also works for making the validation show up on top of the different and separate form inputs, whitch are within the from
                '''
                #error_dict = {}
                error_dict['name'] = "Must input a name here or fill out the student id feild in the number box beside this."
                error_dict['student_number'] = "Must input a student number here or fill out the name feild in the text box beside this."             
                raise forms.ValidationError(error_dict)
                '''
                # this also works for making the validation show up on top of the different and separate form inputs, whitch are within the from
                
                self.add_error('name',"No Student Name was inputed")
                self.add_error('student_number',"No Student Number was inputed")
                         
                # this works for making all validation to show up on top of the whole form
                '''
                raise forms.ValidationError([forms.ValidationError("Must input a name here or fill out the student id feild in the number box beside this."),forms.ValidationError("Must input a student number here or fill out the name feild in the text box beside this.")])
                '''
                # this also works for making all validation to show up on top of the whole form
                '''
                raise forms.ValidationError(["Must input a name here or fill out the student id feild in the number box beside this.","Must input a student number here or fill out the name feild in the text box beside this."])
                '''

        '''
        if student_number !="" or len(student_number)!= 0:
            print("1")
            
            if name !="" or len(name)!= 0:
                print("3")
                
            print("4")
            

        else:
            print("2")
            if name !="" or len(name)!= 0:
                print("5")
                
            else:
                print("6")
                #error_dict['student_number'] = forms.ValidationError("Must input a student number here or fill out the name feild in the text box beside this.")
                #raise forms.ValidationError("Must input a student number here or fill out the name feild in the text box beside this.")
                # dont forget to return or you might see problems with validation

        '''
        

               
