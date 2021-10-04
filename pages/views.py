from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

from django import forms
from form.models import CheckFrequencyForm

# get the model from a different app for it to work
from appointments.models import Appointment
# i must first import connection to execute custom SQL directly
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

import json
from django.http import HttpResponse
#from rest_framework import serializers 
#if you disabled django.middleware.csrf.CsrfViewMiddleware, which is not recommended, you can use csrf_protect() on particular views you want to protect
#i don't need this since the maddleware covers it for all views withought me having to do so myself
#from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
#i just added this
from django.utils import timezone


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #temporarily make log in
        #User.objects.create_user('malinda', 'malinda@sheridancollege.ca', 'malinda', last_login=timezone.now()).save()
        #User.objects.create_user('lydia', 'lydia.novak@sheridancollege.ca', 'lydia', last_login=timezone.now()).save()
        #User.objects.create_user('igbinosa', 'idahosai@sheridancollege.ca', 'igbinosa', last_login=timezone.now()).save()
        
        #u2 = User.objects.create_user('malinda', 'malinda@sheridancollege.ca', 'malinda', last_login=timezone.now())
        #u2.save()
  
        user = auth.authenticate(request, username=username, password=password)
        #will remove later
        #request.session['username'] = username

        if user is not None:
            auth.login(request, user)
            return redirect('/dashboard/')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('index')
        
    else:
        return render(request, 'pages/home.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/overview.html')


def manage_data(request):
    return render(request, 'pages/manageData.html')


def filter_data(request):
    my_form = CheckFrequencyForm()
    context = {'form': my_form}
    return render(request, 'pages/filterData.html', context)


def edit_meeting_comments(request):
    return render(request, 'pages/editmeetingcomments.html')


'''
#----All types of calls to the server(Form GET,Form POST, Ajax GET, Ajax POST) requires a return value back 
#----To take advantage of CSRF protection in your views: ensure that RequestContext is used to render the response 
#so that {% csrf_token %} will work properly. If you’re using the render() function, generic views, or 
# contrib apps, you are covered already since these all use RequestContext.
#----Django sets the csrftoken cookie every time when you request the server, and when you post the data from client to 
# server this token matches that token, If it matches no probs and if not matches it throws an error it is malicious request.
#----Normally the csrf_token template tag will not work if CsrfViewMiddleware.process_view or an equivalent like csrf_protect has not run
#----@ensure_csrf_cookie is the decorator forces a view to send the CSRF cookie, this view don't need it cus it does send 
# a CSRF throught the request in the return. csrf_protect is the decorator that provides the protection of CsrfViewMiddleware 
# to a view. It must be used both on views that insert the CSRF token in the output, and on those that accept the POST form data
'''
#@csrf_protect
def check_frequency(request):
    print(request.GET)
    print(request.POST)

    current_user = request.user 
    
    my_form = CheckFrequencyForm()
    

    if request.method == "POST":
        my_form = CheckFrequencyForm(request.POST or None)
        # my_form.clean_name_n_student_number()
        # my_form.clean_student_number()
        if my_form.is_valid():
            print("BOUT TO PRINT CLEANED DATA ###############################################################################################################")
            print(my_form.cleaned_data)

            lname = 'English class help'
            # --The raw() manager method can be used to perform raw SQL queries that return model instances.
            # --Manager.raw(raw_query, params=None, translations=None) This method takes a raw SQL query, executes it, and returns a
            #  django.db.models.query.RawQuerySet instance. This RawQuerySet instance can be iterated over
            #  like a normal QuerySet to provide object instances.
            # --Django figures out a database table name by joining the model’s “app label” – the name you used in
            #  manage.py startapp – to the model’s class name, with an underscore between them
            # --the {{instance.feildvariable}} that you can call is any in the specified & direct database table, rather than just the
            # django model's feild variable witch may not actually have all the variables of that full table
            # --the plain/basic html {{instance}} iteration on this will begin at the first feild variable of the table that is
            #  declared here so "title" in this case
            '''
            all_data_in_appointments = Appointment.objects.raw('SELECT * FROM appointments_appointment WHERE title = %s', [lname])
            '''
            '''
            all_data_in_appointments = Appointment.objects.raw('SELECT * FROM appointments_appointment')
            '''

            # --when may execute custom sql directly instead of Manager.raw()
            #  Sometimes even Manager.raw() isn’t quite enough: you might need to perform queries that don’t map cleanly to models,
            #  or directly execute UPDATE, INSERT, or DELETE queries. In these cases, you can always access the database directly,
            #  routing around the model layer entirely.
            # --To protect against SQL injection, you must not include quotes around the %s placeholders in the SQL string.
            #  Note that if you want to include literal percent signs in the
            #  query, you have to double them in the case you are passing parameters
            # --the iterator {{instance}} will iterate through the single row when using this('cursor.execute()' + 'fetchone()') way of accessing and it will do so
            #  while following the order of feild variables in the actual direct database, rather than the ones here
            '''
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM appointments_appointment WHERE title = %s', [lname])
                row = cursor.fetchone()
                all_data_in_appointments = row
            '''

            # --the iterator {{instance}} will iterate through the multiple rows when using this('cursor.execute()' + 'fetchall()') way of accessing and it will do so
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

            # all_data_in_appointments.title
            # my_form.save()
            #my_form = CheckFrequencyForm()
            print("***********************************************************************************************This is post")
            #name_of_student = request.POST['studentname']
            #id_of_student = request.POST['studentid']
            #date_of_starting = request.POST['startdate']
            #date_of_end = request.POST['enddate']

            # --the plain/basic html {{instance}} iteration on this will begin at the first feild variable of the table that is
            #  declared here so "title" in this case
            # --the only {{instance.feildvariable}} that you can call is the django model's feild variable witch may
            #  not actually have all the variables of that full table

            #all_data_in_appointments = Appointment.objects.all()

            # wrong rn
            #all_data_in_appointments = Appointment.objects.filter(start_date__range=(datetime.date(2020, 3, 7),datetime.date(2020, 4, 8)), StudentAccount__id__exact = 9516584235, StudentAccount__fname = "First")
            # --end_date is not inclusive according to the doc. Filtering a DateTimeField with dates won’t include items on the last day,
            #  because the bounds are interpreted as “0am on the given date”
            '''
            all_data_in_appointments = Appointment.objects.filter(start_date__range=(datetime.date(2020, 3, 7), datetime.date(2020, 4, 9)))
            '''
            # --tip: save the QuerySet and reuse it cus its cached

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
            # print(type(user_start_date.today().day))
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
                all_data_in_appointments = Appointment.objects.filter(staff_id__id = current_user.id, delete_appointment_row = False, student_id__auth_id__sheridan_id = student_number, start_date__gte=datetime.date(user_start_date.year, user_start_date.month, user_start_date.day), end_date__lte = datetime.date(user_end_date.year, user_end_date.month, user_end_date.day)).select_related("student_id").prefetch_related('student_id__auth_id').order_by("-start_date").values_list('student_id__fname', 'student_id__lname', 'student_id__auth_id__sheridan_id', 'title', 'start_date', 'end_date', 'staff_notes', 'id')
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
                    all_data_in_appointments = Appointment.objects.filter(staff_id__id = current_user.id, delete_appointment_row = False, student_id__fname = firstname_lastname[0], student_id__lname = firstname_lastname[1], start_date__gte=datetime.date(user_start_date.year, user_start_date.month, user_start_date.day), end_date__lte = datetime.date(user_end_date.year, user_end_date.month, user_end_date.day)).select_related("student_id").prefetch_related('student_id__auth_id').order_by("-start_date").values_list('student_id__fname', 'student_id__lname', 'student_id__auth_id__sheridan_id', 'title', 'start_date', 'end_date', 'staff_notes', 'id')
                else:
                    print("44444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444")
                    the_first_name_only = name_of_student
                    print("the_first_name_only is: " + the_first_name_only)
                    print(user_start_date)
                    print(user_end_date)
                    all_data_in_appointments = Appointment.objects.filter(staff_id__id = current_user.id, delete_appointment_row = False, student_id__fname = the_first_name_only, start_date__gte=datetime.date(user_start_date.year, user_start_date.month, user_start_date.day), end_date__lte = datetime.date(user_end_date.year, user_end_date.month, user_end_date.day)).select_related("student_id").prefetch_related('student_id__auth_id').order_by("-start_date").values_list('student_id__fname', 'student_id__lname', 'student_id__auth_id__sheridan_id', 'title', 'start_date', 'end_date', 'staff_notes', 'id')
                
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
                    all_data_in_appointments = Appointment.objects.filter(staff_id__id = current_user.id, delete_appointment_row = False, student_id__fname = firstname_lastname[0], student_id__lname = firstname_lastname[1], student_id__auth_id__sheridan_id = student_number, start_date__gte=datetime.date(user_start_date.year, user_start_date.month, user_start_date.day), end_date__lte = datetime.date(user_end_date.year, user_end_date.month, user_end_date.day)).select_related("student_id").prefetch_related('student_id__auth_id').order_by("-start_date").values_list('student_id__fname', 'student_id__lname', 'student_id__auth_id__sheridan_id', 'title', 'start_date', 'end_date', 'staff_notes', 'id')
                
                else:
                    print("77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777")
                    the_first_name_only = name_of_student
                    print("the_first_name_only is: " + the_first_name_only)
                    all_data_in_appointments = Appointment.objects.filter(staff_id__id = current_user.id, delete_appointment_row = False, student_id__fname = the_first_name_only, student_id__auth_id__sheridan_id = student_number, start_date__gte=datetime.date(user_start_date.year, user_start_date.month, user_start_date.day), end_date__lte = datetime.date(user_end_date.year, user_end_date.month, user_end_date.day)).select_related("student_id").prefetch_related('student_id__auth_id').order_by("-start_date").values_list('student_id__fname', 'student_id__lname', 'student_id__auth_id__sheridan_id', 'title', 'start_date', 'end_date', 'staff_notes', 'id')
                
            #all_data_in_appointments = StudentAccount.objects.filter(auth_id__sheridan_id = 9516584235)
            # context = {'allData': all_data_in_appointments,
            #            'backup': name_of_student,
            #            'form': my_form}

            '''
            context = {'allData': ['jim, dav john'],
                        'backup': name_of_student,
                        'form': my_form}
            '''
            

            #i don't have to serialize the data befor putting it as a context cus thats not the purpose of serialization
            print(all_data_in_appointments)
            print("*******************************************************************************************************************")
            
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
        print("nothing in student number and nameeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        context = {'allData': [""],
                        'backup': name_of_student,
                        'form': my_form}

        return render(request, "pages/filterData.html", context)

    else:
        name_of_student = "jake the man"
        #this actuall shows up on get rather than post
        all_data_in_appointments = [""]
        print(all_data_in_appointments)
        context = {'allData': all_data_in_appointments,
                    'backup': name_of_student,
                     'form': my_form}
        # render Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text
        return render(request, "pages/filterData.html", context)


# def filter_data_search(request):
    # if request.method == 'POST':
        # print(request.POST)
        #dateOne = request.POST.get("start_date")
        #dateTwo = request.POST.get("end_date")

        #studentname = request.POST.get("student_name")
        #studentid = request.POST.get("student_id")

        # request.POST[""]

        #post = Appointment.objects.filter(start_date='**dateOne',end_date='**dateTwo')

        #return render(request, 'pages/filterData.html',{})

'''
#----All types of calls to the server(Form GET,Form POST, Ajax GET, Ajax POST) requires a return value back 
#----i don't think i need it here cus this uses ajax GET
#----The first defense against CSRF attacks is to ensure that GET requests are side effect free 
#----csrf_protect is the decorator that provides the protection of CsrfViewMiddleware to a view. It must be used both on views 
# that insert the CSRF token in the output, and on those that accept the POST form data
'''
#@csrf_protect
def table_load_up(request):
    action_to_take = request.GET.get('actionToTake', None)
    #This doesn't work
    action_to_take2 = request.GET['actionToTake']
    #print("this is ittttttttttttttttttttttttttttttttttttttttttttttt: " + action_to_take + "and action_to_take2 is " + action_to_take2)

    #print("*************************************************************************************************************************")
    # the authentication by default makes & fpopulates the auth_user table in the database, 
    # you can access the attributed by '.' & then <table column name>
    current_user = request.user 
    '''
    print("the current users id issssssssssssssssssssssssssssssssssssssssss")
    print("the current user id: " + str(current_user.id))
    print("the current users name issssssssssssssssssssssssssssssssssssssssss" + str(current_user))
    print("is the current users staff?" + str(current_user.is_staff))
    print("is the current users name?" + str(current_user.username))
    print("is the current users password?" + str(current_user.password))
    '''

    # this is a xml serializer if you want the data transmited as xml
    #data = serializers.serialize("xml", SomeModel.objects.all())
    #i needed to import to make "serializers work
    #Appointment.objects.select_related('student_id__auth_id').all()
    #the select_related lets me reuse. it for feild variables in the model tables here
    



    #prepdata = Appointment.objects.all().select_related('student_id', 'student_id__auth_id').prefetch_related('student_id', 'student_id__auth_id').order_by("-start_date")
    # joins the table together based on specified values
    #Django serializer only serialize queryset, values() and values)list returns valuesQuerySet so it wont work
    #prepdata = Appointment.objects.values_list('title', 'start_date', 'end_date', 'staff_notes', 'student_id__fname','student_id__lname', 'student_id__auth_id__sheridan_id')
    
    #data_table_of_two = list(prepdata) #ValuesQuerySet object needs to be converted to list first
    #dataB = serializers.ListField(data_table_of_two)
    #dataB = json.dumps(data_table_of_two) # convert list to json
    
    datetime.date.today() # Returns 2018-01-15
    #datetime.date.today().time().hour  #datetime.date' object has no attribute 'hour',can't use this for time specifically like in now()
    datetime.datetime.now().time().hour # Returns 2018-01-15 09:00, now() and today() are super similar
    #for select_related() the choice for Appointment are student_id, staff_id, cc_form, ec_form

    #     EFFICIENT FILTER OPTION 0#(LESS EFFICIENT)
    #objectQuerySet = Appointment.objects.filter(start_date__time__lte = datetime.time(datetime.datetime.now().time().hour, datetime.datetime.now().time().minute, datetime.datetime.now().time().second), start_date__lte = datetime.date(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)).select_related("student_id").prefetch_related('student_id__auth_id').order_by("-start_date")
    #******THE BETTER WAY TO COMPARE THEM(DATETIME) IS JUST TO COMPARE THEM AT THESAME TIME SUCH AS LIKE A STRING******
    
    '''
    This is what i should use when the table is fixed today
    objectQuerySet = Appointment.objects.filter(start_date__lte = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, datetime.datetime.now().time().hour, datetime.datetime.now().time().minute, datetime.datetime.now().time().second), staff_id = current_user.id).select_related("student_id").prefetch_related('student_id__auth_id').order_by("-start_date")
    '''


    #datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
    #     EFFICIENT FILTER OPTION 1# (MOST EFFICIENT)
    
    objectQuerySet = Appointment.objects.filter(staff_id__id = current_user.id, delete_appointment_row = False, start_date__lte = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, datetime.datetime.now().time().hour, datetime.datetime.now().time().minute, datetime.datetime.now().time().second)).select_related("student_id").prefetch_related('student_id__auth_id').order_by("-start_date")
    
    #you need the brackests over datetime.datetime.now() if your gonna convert it to string through casting
    #print("TODAYS DATE AND TIME IS:-------------------------------->" + (str)(datetime.datetime.now()))

    #objectQuerySet = Appointment.objects.filter(end_date__lte = datetime.date(user_end_date.year, user_end_date.month, user_end_date.day)).order_by("-start_date")
    #objectQuerySet = Appointment.objects.all().prefetch_related('student_id__auth_id').select_related('student_id', 'student_id__auth_id').order_by("-start_date")
   
    # If p is a Restaurant object, this will give the child class:
    #print(objectQuerySet)

    #print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")

    #print(objectQuerySet.StudentAccount.StudentAuth)

    #print("lllllllllllllllllllllllllllllllllllllllllllllllllllll")

    #print(objectQuerySet)
    #The people who made Django prefer to put all the SQL-affecting methods first, followed (optionally) by any output-affecting methods (such as values())
    #prepdata = Appointment.objects.all().select_related("student_id").prefetch_related('student_id__auth_id').order_by("-start_date").values_list('title', 'start_date', 'end_date', 'staff_notes', 'student_id__fname','student_id__lname', 'student_id__auth_id__sheridan_id')
    #print(prepdata)

    #dataB2 = serializers.serialize('json', list(prepdata), fields=('title', 'start_date', 'end_date', 'staff_notes', 'student_id__fname','student_id__lname', 'student_id__auth_id__sheridan_id'))



    #objectQuerySet = ConventionCard.objects.filter(ownerUser = user)
    #data = serializers.serialize('json', list(objectQuerySet), fields=('fileName','id'))

    #print(ghgh)



    #d = StudentAccount.auth_id
    #prepdata = Appointment.objects.all().prefetch_related('student_id__auth_id')


    #objectQuerySet2 = Appointment.objects.filter(start_date__lte = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, datetime.datetime.now().time().hour, datetime.datetime.now().time().minute, datetime.datetime.now().time().second), staff_id = current_user.id).select_related("student_id").prefetch_related('student_id__auth_id').order_by("-start_date").values_list("id","student_id__auth_id__sheridan_id", 'student_id__fname', "student_id__lname", "title", "start_date", "end_date", "staff_notes")
    
    #objectQuerySet2 = Appointment.objects.filter(start_date__lte = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, datetime.datetime.now().time().hour, datetime.datetime.now().time().minute, datetime.datetime.now().time().second), staff_id = current_user.id).select_related("student_id").prefetch_related('student_id__auth_id').order_by("-start_date").values("id","student_id__auth_id__sheridan_id", 'student_id__fname', "student_id__lname", "title", "start_date", "end_date", "staff_notes")
    #print("this is objectQueryset2 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    #print(list(objectQuerySet2.all()))


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
    #objectQuerySet = Appointment.objects.all()
    #all_objects = [*objectQuerySet, *objectQuerySet.studentAccount, *objectQuerySet.studentAccount.studentauth]
    #dataB = serializers.serialize('json', all_objects)
    

    '''
    The default serialization strategy for foreign keys and many-to-many relations is to serialize the value of the 
    primary key(s) of the objects in the relation. This strategy works well for most objects, but it can cause 
    difficulty in some circumstances.
    There is also the matter of convenience. An integer id isn’t always the most convenient way to refer to an object; 
    sometimes, a more natural reference would be helpful. It is for these reasons that Django provides natural keys. 
    A natural key is a tuple of values that can be used to uniquely identify an object instance without using the primary key value.
    '''
    '''
    dataB = serializers.serialize("json", objectQuerySet)
    '''
    '''
    When use_natural_foreign_keys=True is specified, Django will use the natural_key() method to serialize any foreign key 
    reference to objects of the type that defines the method. When use_natural_primary_keys=True is specified, Django will 
    not provide the primary key in the serialized data of this object since it can be calculated during deserialization:
    '''
    '''
    When use_natural_primary_keys=True is specified, Django will not provide the primary key in the serialized 
    data of this object since it can be calculated during deserialization:
    '''
    #this works but WE NEED TO REDUCE THE feilds displayed so we won't use this
    #dataB = serializers.serialize("json", objectQuerySet, use_natural_foreign_keys=True, use_natural_primary_keys=False)
    
    dataB = serializers.serialize("json", objectQuerySet, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=['student_id', 'title', 'start_date', 'end_date', 'staff_notes'])
    #dataB2 = serializers.serialize("json", objectQuerySet2, use_natural_foreign_keys=True, use_natural_primary_keys=True)
    '''
    print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
    print(type(objectQuerySet))
    print(str(objectQuerySet))
    print("serialized type version of above")
    print(type(dataB))
    print(str(dataB))
    print("next type")
    '''
    #print(type(objectQuerySet2))
    #print("string type of above, maybe i should serialize this")
    #print(objectQuerySet2)
    #print(type(dataB2))
    #dataB = json.loads(serializers.serialize('json', [prepdata]))[0]
    #print("this is dataB +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    #print(dataB)

    #data3 = serializers.serialize("json", prepdata.auth_id())
    
    #Appointment.objects.select_related('blog')
    
    response = {
        'allData': dataB #,
        #'allDataStudentAccount': str(objectQuerySet2) #,
        #'allDataStudentAuth': data3
    }
    
    #response = objectQuerySet2
    '''
    response = {
        'allDataStudentAccount': str(objectQuerySet2) #,
        #'allDataStudentAuth': data3
    }
    '''
    # i needed to make an import to have "JsonResponse" work
    '''
    does jsonresponse use RequestContext??:
    https://docs.djangoproject.com/en/dev/ref/csrf/#ajax
    '''
    return JsonResponse(response)
    # i must install "from django.http import HttpResponse" to use this   
    #return HttpResponse(response)

'''
#----All types of calls to the server(Form GET,Form POST, Ajax GET, Ajax POST) requires a return value back 
#----csrf_protect is the decorator that provides the protection of CsrfViewMiddleware to a view. It must be used both on views that insert the CSRF token in the output, and on those that accept the POST form data
'''
#@csrf_protect
def table_row_delete(request):
    print("We are in table_row_delete")
    #id_to_delete = request.POST('actionToTake', None)
    #this below code seems to give an error of MultiValueDictKeyError: 'actionToTake'
    #id_to_delete = request.POST['actionToTake']
    id_to_delete = request.POST.get('actionToTake')
    #print("this is the Appointment id that we will delete: " + id_to_delete)

    Appointment.objects.filter(pk=id_to_delete).update(delete_appointment_row = True)

    
    current_user = request.user 
    #get table data for appointments that have no staff comment
    objectQuerySetTableTwo = Appointment.objects.filter(staff_id__id = current_user.id, delete_appointment_row = False, staff_notes__isnull=True, start_date__lte = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, datetime.datetime.now().time().hour, datetime.datetime.now().time().minute, datetime.datetime.now().time().second)).select_related("student_id").prefetch_related('student_id__auth_id').order_by("-start_date")
    dataC = serializers.serialize("json", objectQuerySetTableTwo, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=['student_id', 'title', 'start_date', 'end_date', 'staff_notes'])
    

    #request.POST['actionToTake']
    #i don't think i have to validate the post cus the user didn't type up that input ans send it, 
    # it is a number that the system is sending to itself
    #Appointment.objects.filter(pk=id_to_delete).delete()
    response = { 'id_to_delete':id_to_delete,
                'allDataTableTwo': dataC
    }
    #return
    return JsonResponse(response)
    #this just gave an error
    #return render(request, response, {})


def table_row_add_capture_all(request):
    print("We are in table_row_add_capture_all")
    id_to_add = request.POST.get('actionToTake')
    #print("this is the Appointment id that we will add: " + id_to_add)

    # the authentication by default makes & populates the auth_user table in the database, 
    # you can access the attributed by '.' & then <table column name>
    current_user = request.user 


    '''
    #if no id match then this way will give an error
    t = Appointment.objects.get(id=id_to_add)
    t.value = id_to_add  # change field
    t.save() # this will update only
    '''


    # alternate option to updating a new column
    Appointment.objects.filter(id=id_to_add).update(delete_appointment_row = False)

    


    # ?? is doing (staff_id = vurrent_user.id) safer than (staff_id__id = current_user.id). since it's a foreigh key it should be thesame amount
    #  of safeness
    #    
    objectQuerySet = Appointment.objects.filter(staff_id__id = current_user.id, delete_appointment_row = False, start_date__lte = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, datetime.datetime.now().time().hour, datetime.datetime.now().time().minute, datetime.datetime.now().time().second)).select_related("student_id").prefetch_related('student_id__auth_id').order_by("-start_date")
    dataB = serializers.serialize("json", objectQuerySet, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=['student_id', 'title', 'start_date', 'end_date', 'staff_notes'])
    
    #get table data for appointments that have no staff comment
    objectQuerySetTableTwo = Appointment.objects.filter(staff_id__id = current_user.id, delete_appointment_row = False, staff_notes__isnull=True, start_date__lte = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, datetime.datetime.now().time().hour, datetime.datetime.now().time().minute, datetime.datetime.now().time().second)).select_related("student_id").prefetch_related('student_id__auth_id').order_by("-start_date")
    dataC = serializers.serialize("json", objectQuerySetTableTwo, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=['student_id', 'title', 'start_date', 'end_date', 'staff_notes'])
    

    #print(dataB)
    
    response = {
        'allData': dataB,
        'allDataTableTwo': dataC
    }
    return JsonResponse(response)


def table_load_up_deletions(request):
    #action_to_take = request.GET.get('actionToTake', None)
    #This doesn't work
    #action_to_take2 = request.GET['actionToTake']
    #print("this is action_to_takeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee: " + action_to_take + "and action_to_take2 is " + action_to_take2)
    print("you are in table_load_up_deletions")
    #print("*************************************************************************************************************************")
    # the authentication by default makes & fpopulates the auth_user table in the database, 
    # you can access the attributed by '.' & then <table column name>
    current_user = request.user 

    
    objectQuerySet = Appointment.objects.filter(staff_id__id = current_user.id, delete_appointment_row = True, start_date__lte = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, datetime.datetime.now().time().hour, datetime.datetime.now().time().minute, datetime.datetime.now().time().second)).select_related("student_id").prefetch_related('student_id__auth_id').order_by("-start_date")

    dataB = serializers.serialize("json", objectQuerySet, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=['student_id', 'title', 'start_date', 'end_date', 'staff_notes'])
    
    #print(dataB)
    print("you are out table_load_up_deletions")
    response = {
    'allData': dataB
    }
    return JsonResponse(response)

def table_load_up_empty_staff_notes(request):
    action_to_take = request.GET.get('actionToTake', None)
    print("you are in table_load_up_empty_staff_notes")
    #This doesn't work
    #action_to_take2 = request.GET['actionToTake']
    #print("this is action_to_takeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee: " + action_to_take + "and action_to_take2 is " + action_to_take2)
    print("is staf notes loadingggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg")
    #print("*************************************************************************************************************************")
    # the authentication by default makes & fpopulates the auth_user table in the database, 
    # you can access the attributed by '.' & then <table column name>
    current_user = request.user 

    
    objectQuerySet = Appointment.objects.filter(staff_id__id = current_user.id, delete_appointment_row = False, staff_notes__isnull=True, start_date__lte = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, datetime.datetime.now().time().hour, datetime.datetime.now().time().minute, datetime.datetime.now().time().second)).select_related("student_id").prefetch_related('student_id__auth_id').order_by("-start_date")
    print(str(objectQuerySet))
    print("NEXTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
    print(objectQuerySet)
    dataB = serializers.serialize("json", objectQuerySet, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=['student_id', 'title', 'start_date', 'end_date', 'staff_notes'])
    
    #print(dataB)
    print("you are out table_load_up_empty_staff_notes")
    response = {
    'allData': dataB
    }
    return JsonResponse(response)


def managedata_table_row_to_edit_page(request):
    print("you are in managedata_table_row_to_edit_page")
    action_to_take = request.GET.get('actionToTake', None)
    #This doesn't work
    action_to_take2 = request.GET['actionToTake']
    #print("this is action_to_takeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee: " + action_to_take + "and action_to_take2 is " + action_to_take2)
    print("------------------------------------------Going to editcommentpage now")
    #print("*************************************************************************************************************************")
    print("you are out managedata_table_row_to_edit_page")
    response = {
    'redirectpageid': action_to_take
    }
    return JsonResponse(response)
    #here = "editmeetingcomments"
    #return here

#put id as parameter to accept id that will be passed from html
def manageData_post_to_edit_meeting_comments(request, id):

    print("i am in the editmeetingcomments.html that came after the manageData page")
    current_user = request.user 


    one_data_in_appointments = Appointment.objects.filter(staff_id__id = current_user.id, delete_appointment_row = False, id = id).select_related("student_id").prefetch_related('student_id__auth_id').order_by("-start_date").values_list('student_id__fname', 'student_id__lname', 'student_id__auth_id__sheridan_id', 'title', 'start_date', 'end_date', 'staff_notes')
    #dataB = serializers.serialize("json", objectQuerySet, use_natural_foreign_keys=True, use_natural_primary_keys=False)


    #context = {'idfrommanagedata': id}


    context = {'allData': one_data_in_appointments,
               'idfrommanagedata': id
               }

    return render(request, "pages/editmeetingcomments.html", context)


def editmeeting_save_meeting_comments(request):
    print("we made it in editmeeting_save_meeting_comments")
    current_user = request.user
    idfromappointment = request.POST.get('pastpageappointmentid', None)
    writtenwords = request.POST.get('writtenwords', None)

    print(idfromappointment)
    print("that was the id")
    print(type(idfromappointment))

    if request.method == "POST":
        #yup this doesn't work
        #idfromappointment = request.POST['pastpageappointmentid']
        print(idfromappointment)
        print("that was the id again")
        print(type(idfromappointment))

        #this way if the id don't exist then it won't make an error 
        if (idfromappointment):
             # alternate option to updating a new column

            Appointment.objects.filter(id = idfromappointment, staff_id__id = current_user.id).update(staff_notes = writtenwords)

            #one_data_in_appointments = Appointment.objects.filter(staff_id__id = current_user.id, staff_notes = writtenwords, id = idfromappointment)

    return render(request, "pages/editmeetingcomments.html", {})

   

def load_staff_forms_on_filterdata_page(request):
    print("you are in load_staff_forms_on_filterdata_page")
    current_user = request.user
    idfromappointmentfdpage = request.GET.get('actionToTake', None)
   
    firstvisit = Appointment.objects.filter(id=idfromappointmentfdpage).count()

    

    context = {}

    #Lydia Novak
    if (current_user.id == 6):
        #in the values_list() function dont' forget the put the current object's variable + "__" befor you put the foreighkey variable that you want to access
        #all_form_info = Appointment.objects.filter(staff_id__id = current_user.id, delete_appointment_row = False, id = idfromappointmentfdpage).select_related("cc_form").values_list('id' ,'q1c_sso', 'q1c_friend', 'q1c_faculty', 'q1c_visit', 'q1c_orient', 'q1c_event', 'q1c_kpi', 'q1c_outreach', 'q1c_posters', 'q1c_stv', 'q1c_social', 'q1c_media', 'q1c_walkby', 'q1c_website', 'ccs_exploration', 'ccs_eplanning', 'ccs_cplanning', 'ccs_labourmarket', 'ccs_other')
        #I NEED TO remove THE values_list() when i serialize and return it as a JsonResponse. this is different from render
        #all_form_info = Appointment.objects.filter(staff_id__id = current_user.id, delete_appointment_row = False, id = idfromappointmentfdpage).select_related("cc_form").values_list('id' ,'cc_form__q1c_sso', 'cc_form__q1c_friend', 'cc_form__q1c_faculty', 'cc_form__q1c_visit', 'cc_form__q1c_orient', 'cc_form__q1c_event', 'cc_form__q1c_kpi', 'cc_form__q1c_outreach', 'cc_form__q1c_posters', 'cc_form__q1c_stv', 'cc_form__q1c_social', 'cc_form__q1c_media', 'cc_form__q1c_walkby', 'cc_form__q1c_website', 'cc_form__ccs_exploration', 'cc_form__ccs_eplanning', 'cc_form__ccs_cplanning', 'cc_form__ccs_labourmarket', 'cc_form__ccs_other')
        #blocking this currently cus it don't have order_by("-start_date")
        #all_form_info = Appointment.objects.filter(staff_id__id = current_user.id, delete_appointment_row = False, id = idfromappointmentfdpage).select_related("cc_form")
        #im adding order_by("-start_date") to the end
        all_form_info = Appointment.objects.filter(staff_id__id = current_user.id, delete_appointment_row = False, id = idfromappointmentfdpage).select_related("cc_form").order_by("-start_date")
        #remember than id won't show up when u put feild=[] cus that is a defaultly and unexplicitly added feild in the model object
        dataB = serializers.serialize("json", all_form_info, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields = ['submission_date', 'student_id','cc_form'])
        print(dataB)
        context = {'allforminfo': dataB,
                'idfromappointmentfdpage': 6,
                'firstvisit': firstvisit}


    #Melina Elia
    if (current_user.id == 7):
        #in the values_list() function dont' forget the put the current object's variable + "__" befor you put the foreighkey variable that you want to access
        #all_form_info = Appointment.objects.filter(staff_id__id = current_user.id, delete_appointment_row = False, id = idfromappointmentfdpage).select_related("ec_form").values_list('id' , 'q1e_sso', 'q1e_friend', 'q1e_faculty', 'q1e_visit', 'q1e_orient', 'q1e_event', 'q1e_kpi2', 'q1e_outreach', 'q1e_posters', 'q1e_stv', 'q1e_social', 'q1e_media', 'q1e_walkby', 'q1e_website', 'ecs_resume', 'ecs_cover', 'ecs_interview', 'ecs_jobsearch', 'ecs_mockinterview', 'ecs_networking', 'ecs_portfolio')
        #I NEED TO remove THE values_list() when i serialize and return it as a JsonResponse. this is different from render
        #all_form_info = Appointment.objects.filter(staff_id__id = current_user.id, delete_appointment_row = False, id = idfromappointmentfdpage).select_related("ec_form").values_list('id' , 'ec_form__q1e_sso', 'ec_form__q1e_friend', 'ec_form__q1e_faculty', 'ec_form__q1e_visit', 'ec_form__q1e_orient', 'ec_form__q1e_event', 'ec_form__q1e_kpi2', 'ec_form__q1e_outreach', 'ec_form__q1e_posters', 'ec_form__q1e_stv', 'ec_form__q1e_social', 'ec_form__q1e_media', 'ec_form__q1e_walkby', 'ec_form__q1e_website', 'ec_form__ecs_resume', 'ec_form__ecs_cover', 'ec_form__ecs_interview', 'ec_form__ecs_jobsearch', 'ec_form__ecs_mockinterview', 'ec_form__ecs_networking', 'ec_form__ecs_portfolio')
        #blocking this currently cus it don't have order_by("-start_date")
        #all_form_info = Appointment.objects.filter(staff_id__id = current_user.id, delete_appointment_row = False, id = idfromappointmentfdpage).select_related("ec_form")
        #im adding order_by("-start_date") to the end
        all_form_info = Appointment.objects.filter(staff_id__id = current_user.id, delete_appointment_row = False, id = idfromappointmentfdpage).select_related("ec_form").order_by("-start_date")
        dataB = serializers.serialize("json", all_form_info, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields = ['submission_date', 'student_id', 'ec_form'])
        print(dataB)
        context = {'allforminfo': dataB,
                    'idfromappointmentfdpage': 7,
                    'firstvisit': firstvisit}


    print(all_form_info)
    print("end of load_staff_forms_on_filterdata_page")

    return JsonResponse(context)
    #return render(request, "pages/filterData.html", context)