from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

from django import forms
from form.models import CheckFrequencyForm

# get the model from a different app for it to work
from appointments.models import Appointment
#i must first import connection to execute custom SQL directly
from django.db import connection
# Create your views here.
import datetime

from studentauth.models import StudentAuth
from student.models import StudentAccount
# i need this so i can use regex
import re
# i need to get rid of messages cus i dont need it
from django.contrib import messages
from django.http import JsonResponse
from django.core import serializers

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('index')
    else:
        return render(request, 'pages/home.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'pages/dashboard.html')


def manage_data(request):
    return render(request, 'pages/manageData.html')


def filter_data(request):
    my_form = CheckFrequencyForm()
    context = {'form': my_form}
    return render(request, 'pages/filterData.html', context)


def edit_meeting_comments(request):
    return render(request, 'pages/editmeetingcomments.html')


def check_frequency(request):
    print(request.GET)
    print(request.POST)
    my_form = CheckFrequencyForm()
    if request.method == "POST":
        my_form = CheckFrequencyForm(request.POST or None)
        #my_form.clean_name_n_student_number()
        #my_form.clean_student_number()
        if my_form.is_valid():
            print("BOUT TO PRINT CLEANED DATA ###############################################################################################################")
            print(my_form.cleaned_data)


            lname = 'English class help'
            #--The raw() manager method can be used to perform raw SQL queries that return model instances.
            #--Manager.raw(raw_query, params=None, translations=None) This method takes a raw SQL query, executes it, and returns a 
            #  django.db.models.query.RawQuerySet instance. This RawQuerySet instance can be iterated over 
            #  like a normal QuerySet to provide object instances.
            #--Django figures out a database table name by joining the model’s “app label” – the name you used in
            #  manage.py startapp – to the model’s class name, with an underscore between them
            #--the {{instance.feildvariable}} that you can call is any in the specified & direct database table, rather than just the 
            # django model's feild variable witch may not actually have all the variables of that full table
            #--the plain/basic html {{instance}} iteration on this will begin at the first feild variable of the table that is 
            #  declared here so "title" in this case
            '''
            all_data_in_appointments = Appointment.objects.raw('SELECT * FROM appointments_appointment WHERE title = %s', [lname])
            '''
            '''
            all_data_in_appointments = Appointment.objects.raw('SELECT * FROM appointments_appointment')
            '''

            #--when may execute custom sql directly instead of Manager.raw()
            #  Sometimes even Manager.raw() isn’t quite enough: you might need to perform queries that don’t map cleanly to models, 
            #  or directly execute UPDATE, INSERT, or DELETE queries. In these cases, you can always access the database directly, 
            #  routing around the model layer entirely.
            #--To protect against SQL injection, you must not include quotes around the %s placeholders in the SQL string.
            #  Note that if you want to include literal percent signs in the 
            #  query, you have to double them in the case you are passing parameters
            #--the iterator {{instance}} will iterate through the single row when using this('cursor.execute()' + 'fetchone()') way of accessing and it will do so
            #  while following the order of feild variables in the actual direct database, rather than the ones here
            '''
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM appointments_appointment WHERE title = %s', [lname])
                row = cursor.fetchone()
                all_data_in_appointments = row
            '''

            #--the iterator {{instance}} will iterate through the multiple rows when using this('cursor.execute()' + 'fetchall()') way of accessing and it will do so
            #  while following the order of feild variables in the actual direct database, rather than the ones here
            '''
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM appointments_appointment')
                row = cursor.fetchall()
                all_data_in_appointments = row
            '''
            '''
            #--^ same as v--
            cursor = connection.cursor()
            try:
                cursor.execute('SELECT * FROM appointments_appointment')
            finally:
                #--you must access the cursor method befor the close() is called or it will give you an error.
                #--the {{instance.feildvariable}} shouldn't be called in this way if you use fetchall() cus it dont make sense
                row = cursor.fetchone()
                all_data_in_appointments = row
                cursor.close()
            '''

            #all_data_in_appointments.title
            #my_form.save()
            #my_form = CheckFrequencyForm()
            print("***********************************************************************************************This is post")
            #name_of_student = request.POST['studentname']
            #id_of_student = request.POST['studentid']
            #date_of_starting = request.POST['startdate']
            #date_of_end = request.POST['enddate']

            
            
            #--the plain/basic html {{instance}} iteration on this will begin at the first feild variable of the table that is 
            #  declared here so "title" in this case
            #--the only {{instance.feildvariable}} that you can call is the django model's feild variable witch may 
            #  not actually have all the variables of that full table
            
            #all_data_in_appointments = Appointment.objects.all()
            
            #wrong rn
            #all_data_in_appointments = Appointment.objects.filter(start_date__range=(datetime.date(2020, 3, 7),datetime.date(2020, 4, 8)), StudentAccount__id__exact = 9516584235, StudentAccount__fname = "First")
            #--end_date is not inclusive according to the doc. Filtering a DateTimeField with dates won’t include items on the last day, 
            #  because the bounds are interpreted as “0am on the given date”
            '''
            all_data_in_appointments = Appointment.objects.filter(start_date__range=(datetime.date(2020, 3, 7), datetime.date(2020, 4, 9)))
            '''
            #--tip: save the QuerySet and reuse it cus its cached
            
            #all_data_in_appointments = Appointment.objects.filter(start_date__gte=datetime.date(2020, 3, 7), end_date__lte = datetime.date(2020, 4, 9))
            
            
            #all_data_in_appointments = Appointment.objects.filter(student_id__auth_id_id__sheridan_id = 9516584235)


            

            # this is how you get the request data when you use form models
            student_number = my_form.cleaned_data['student_number']
            #the begining spaces and ending spaces do not get stored in here when it collects user input so less work for us
            name_of_student = my_form.cleaned_data['name']
            user_start_date = my_form.cleaned_data['start_date']
            user_end_date = my_form.cleaned_data['end_date']
            print("see if it get correct dataaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            print(name_of_student)
            print(type(name_of_student))
            #student_number is a NoneType if no number is typed up by user in the student number input form
            print(student_number)
            print(type(student_number))
            print(user_start_date)
            #print(type(user_start_date.today().day))
            print(user_end_date)
            

            print(user_start_date.day)
            print(user_end_date.month)
            print(user_end_date.year)

            print(type(user_start_date.today().day))
            print(type(user_start_date.today().month))
            print(type(user_start_date.today().year))
            print("***************************************************")
            print("name_of_student is: " + name_of_student)

            #if empty
            if (name_of_student == "" or len(name_of_student)== 0):
                print("11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")
                # i think that this would work. This one says auth_id witch is exactly in the model made her about the database
                #must student_number be converted iinto a string befor i can check it against the datbase?
                all_data_in_appointments = Appointment.objects.filter(student_id__auth_id__sheridan_id = student_number, start_date__gte=datetime.date(user_start_date.year, user_start_date.month, user_start_date.day), end_date__lte = datetime.date(user_end_date.year, user_end_date.month, user_end_date.day))
                # this one should also work
                # this one says auth_id_id witch is exact as in the database
                #all_data_in_appointments = Appointment.objects.filter(student_id__auth_id_id__sheridan_id = student_number, start_date__gte=datetime.date(user_start_date.year, user_start_date.month, user_start_date.day), end_date__lte = datetime.date(user_end_date.year, user_end_date.month, user_end_date.day))
                # i have confirmed that both of those work

            #if empty
            #how to check if integer has a value
            #elif (str(student_number) == "" or len(str(student_number)) == 0):
            
            #elif (student_number is None):
            elif(student_number ==None):
                print("2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222")
                if((" " in name_of_student) == True):
                    print("33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333")
                    striped_name = name_of_student.strip()
                    #striped_name.replace(" ", "")
                    print("name_of_student.strip() = : " + name_of_student.strip())
                    print("striped name is: " + striped_name)
                    #turned to a list of teh first name and last name

                    #firstname_lastname = striped_name.split(" ")
                    firstname_lastname = re.split("\W+", striped_name)
                    print("firstname_lastname is: " + firstname_lastname[0] + firstname_lastname[1])
                    all_data_in_appointments = Appointment.objects.filter(student_id__fname = firstname_lastname[0], student_id__lname = firstname_lastname[1], start_date__gte=datetime.date(user_start_date.year, user_start_date.month, user_start_date.day), end_date__lte = datetime.date(user_end_date.year, user_end_date.month, user_end_date.day))
                else:
                    print("44444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444")
                    the_first_name_only = name_of_student
                    print("the_first_name_only is: " + the_first_name_only)
                    all_data_in_appointments = Appointment.objects.filter(student_id__fname = the_first_name_only, start_date__gte=datetime.date(user_start_date.year, user_start_date.month, user_start_date.day), end_date__lte = datetime.date(user_end_date.year, user_end_date.month, user_end_date.day))
                
            else:
                print("55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555")
                if((" " in name_of_student) == True):
                    print("6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666")
                    striped_name = name_of_student.strip()
                    #striped_name.replace(" ", "")
                    #s.replace(" ", "")        
                    print("name_of_student.strip() = : " + name_of_student.strip())
                    print("striped name is: " + striped_name)
                    #turned to a list of the first name and last name
                    #this doesn't work
                    #firstname_lastname = striped_name.split(r'\W') #r'[\s]'
                    # this works but i must import re first
                    firstname_lastname = re.split("\W+", striped_name)
                    #r'[^\w]'
                    print("going into first_lastname: ")
                    for h in firstname_lastname:
                        print("_]"+h+"[_")

                    print("out of the loop")
                    print("firstname_lastname is: " + firstname_lastname[0] + firstname_lastname[1])
                    #so i can't send a NoneType student_number value to check against the database
                    all_data_in_appointments = Appointment.objects.filter(student_id__fname = firstname_lastname[0], student_id__lname = firstname_lastname[1], student_id__auth_id__sheridan_id = student_number, start_date__gte=datetime.date(user_start_date.year, user_start_date.month, user_start_date.day), end_date__lte = datetime.date(user_end_date.year, user_end_date.month, user_end_date.day))
                
                else:
                    print("77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777")
                    the_first_name_only = name_of_student
                    print("the_first_name_only is: " + the_first_name_only)
                    all_data_in_appointments = Appointment.objects.filter(student_id__fname = the_first_name_only, student_id__auth_id__sheridan_id = student_number, start_date__gte=datetime.date(user_start_date.year, user_start_date.month, user_start_date.day), end_date__lte = datetime.date(user_end_date.year, user_end_date.month, user_end_date.day))
                
            #all_data_in_appointments = StudentAccount.objects.filter(auth_id__sheridan_id = 9516584235)
            #context = {'allData': all_data_in_appointments,
            #            'backup': name_of_student,
            #            'form': my_form}

            '''
            context = {'allData': ['jim, dav john'],
                        'backup': name_of_student,
                        'form': my_form}
            '''
            
            context = {'allData': all_data_in_appointments,
                        #backup show be changed to search_result_frequency ?????????????????????????????????????????????????
                        'backup': name_of_student,
                        'form': my_form}
            return render(request, "pages/filterData.html", context)
        else:
            #print("BOUT TO PRINT CLEANED DATA ERRORS ###############################################################################################################")
            #validation error came up
            print(my_form.errors)
            # im using message to print errors
            


        messages.error(request,my_form.errors) 
    
        #this runs if we have a empty student_number and name_of_student
        name_of_student = 'studentname'
        context = {'allData': [""],
                        'backup': name_of_student,
                        'form': my_form}

        return render(request, "pages/filterData.html", context)

    else:
        name_of_student = "jake the man"
        #this actuall shows up on get rather than post
        all_data_in_appointments = ""
        context = {'allData': all_data_in_appointments,
                    'backup': name_of_student,
                     'form': my_form}

        return render(request, "pages/filterData.html", context)


#def filter_data_search(request):
    #if request.method == 'POST':
        #print(request.POST)
        #dateOne = request.POST.get("start_date")
        #dateTwo = request.POST.get("end_date")
        
        #studentname = request.POST.get("student_name")
        #studentid = request.POST.get("student_id")

        #request.POST[""]
     
        #post = Appointment.objects.filter(start_date='**dateOne',end_date='**dateTwo')

        #return render(request, 'pages/filterData.html',{})

def table_load_up(request):
    username = request.GET.get('actionToTake', None)
    print("this is ittttttttttttttttttttttttttttttttttttttttttttttt: " + username)
    # this is a xml serializer if you want the data transmited as xml
    #data = serializers.serialize("xml", SomeModel.objects.all())
    #i needed to import to make "serializers work
    #Appointment.objects.select_related('student_id__auth_id').all()
    #the select_related lets me reuse. it for feild variables in the model tables here
    
    prepdata = Appointment.objects.all().prefetch_related('student_id__auth_id').select_related('student_id', 'student_id__auth_id').order_by("-start_date")
    #d = StudentAccount.auth_id
    #prepdata = Appointment.objects.all().prefetch_related('student_id__auth_id')



    #THIS IS THE ONE THAT WORKS!!!
    #prepdata = Appointment.objects.filter(student_id__auth_id__sheridan_id = 9516584235).prefetch_related('student_id__auth_id', 'student_id')

    #predata2 = prepdata.as_manager().StudentAuth.objects.all()
    #prepdata2 = list(Appointment.objects.all())
    #print(prepdata.values("student_id__auth_id__sheridan_id", 'student_id__fname', "student_id__lname", "title", "start_date", "end_date", "staff_notes"))
    #Manager.obj
    

    #print(prepdata2)

    #data = serializers.serialize("json", prepdata)
    
    #prepdata.allDataStudentAccount
    
    #print("data.student_id: "+prepdata.student_id.all())
    dataB = serializers.serialize("json", prepdata)
    #data3 = serializers.serialize("json", prepdata.auth_id())
    
    #Appointment.objects.select_related('blog')
    
    response = {
        'allData': dataB ,
        'allDataStudentAccount': 6 #,
        #'allDataStudentAuth': data3
    }
    # i needed to make an import to have "JsonResponse" work
    return JsonResponse(response)
