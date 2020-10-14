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
    #my_form = CheckFrequencyForm()
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
            name_of_student = request.POST['studentname']
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
            
            all_data_in_appointments = Appointment.objects.filter(start_date__gte=datetime.date(2020, 3, 7), end_date__lte = datetime.date(2020, 4, 9))
            
            #context = {'allData': all_data_in_appointments,
            #            'backup': name_of_student,
            #            'form': my_form}

            '''
            context = {'allData': ['jim, dav john'],
                        'backup': name_of_student,
                        'form': my_form}
            '''
            
            context = {'allData': all_data_in_appointments,
                        'backup': name_of_student,
                        'form': my_form}
            return render(request, "pages/filterData.html", context)
        else:
            print("BOUT TO PRINT CLEANED DATA ERRORS ###############################################################################################################")
            print(my_form.errors)
            


        name_of_student = request.POST['studentname']
        context = {'allData': ['jim, dav john'],
                        'backup': name_of_student,
                        'form': my_form}

        return render(request, "pages/filterData.html", context)

    else:
        name_of_student = "jake the man"
        all_data_in_appointments = "nothing in context"
        context = {'allData': all_data_in_appointments,
                    'backup': name_of_student}

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