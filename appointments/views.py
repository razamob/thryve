from django.shortcuts import render, redirect
from .models import Appointment
from rest_framework.renderers import TemplateHTMLRenderer
from django.core import serializers
from rest_framework import viewsets
from .serializers import AppointmentSerializer
from staff.models import StaffAccount
from student.models import StudentAccount
from staff.models import StaffAuth
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib import messages
import json
import datetime
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dateutil import parser


class AppointmentView(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'appointments/appointments.html'
    queryset = Appointment.objects.all()

    def list(self, request):
        queryset = Appointment.objects.all().values()
        # appointments = [
        #     appointment.title for appointment in Appointment.objects.all()]
        return JsonResponse({"appointments": list(queryset)})

    def create(self, request):
        # send_mail(
        #     'Hello Mobeen',
        #     'MOBEEN RAZA HELLO APPOINTMENT',
        #     'mobeenraza39@gmail.com',
        #     ['mobeenraza39@gmail.com'],
        #     fail_silently=False
        # )
        print(request.POST)
        username = request.user.username
        user = StaffAccount.objects.get(email=username)
        userID = user.auth_id.id + 1
        userlogin = StaffAuth.objects.get(username=username)
        email = request.POST.get('email')
        start_date = parser.parse(request.POST.get('start_date')).timestamp()
        end_date = parser.parse(request.POST.get('end_date')).timestamp()
        student = StudentAccount.objects.create(
            fname=request.POST.get('fname'),
            lname=request.POST.get('lname'),
            email=email,
            student_number=request.POST.get('studentid')
        )
        for each in Appointment.objects.all():
            if (start_date >= each.start_date.timestamp() and start_date <= each.end_date.timestamp()) or (end_date >= each.start_date.timestamp() and end_date <= each.end_date.timestamp()):
                messages.error(
                    request, 'Appointment for this date is already booked.')
                return redirect('/appointments/')
        appointment = Appointment.objects.create(
            title=request.POST.get('title'),
            start_date=request.POST.get('start_date'),
            end_date=request.POST.get('end_date'),
            description=request.POST.get('description'),
            staff_id=user,
            student_id=student,
            delete_appointment_row=False
        )

        serializer = AppointmentSerializer(appointment)
        appointments = Appointment.objects.filter(
            staff_id=userID)
        students = StudentAccount.objects.filter(
            id=appointment.student_id.id)

        message = Mail(
            from_email='mobeenraza39@gmail.com',
            to_emails=email,
            subject='Your appointment is booked for ' +
            request.POST.get('start_date'),
            html_content=request.POST.get('description'))
        try:
            sg = SendGridAPIClient(
                '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')
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)
        messages.success(
            request, 'Your appointment has been booked.')
# # "Appointment for " + request.POST.get('fname') + " " + request.POST.get(
#     'lname') + " on " + request.POST.get('start_date'),
# "Hi " + request.POST.get('fname') + ". This is to confirm that your appointment is set for " +
# request.POST.get('start_date') + ".",
        return render(request, 'appointments/appointments.html', {'user': user, 'userlogin': userlogin, 'appointments': appointments, 'students': students})
        # appointments = Appointment.objects.all()

        # # return render(request, 'appointments/appointments.html', {'appointments': appointments})
        # return render(request, 'appointments/appointments.html', {'appointments': appointments})

    # def destroy(self, request, pk):
    #     appointment = Appointment.objects.get(id=pk)
    #     appointment.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class AppointmentAPI(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


def index(request):
    username = request.user.username
    user = StaffAccount.objects.get(email=username)
    userID = user.auth_id.id
    userlogin = StaffAuth.objects.get(username=username)
    print(user.auth_id)
    appointments = Appointment.objects.filter(
        staff_id=userID)
    # students = StudentAccount.objects.filter(
    #     StudentAccount.id == appointments.student_id)
    return render(request, 'appointments/appointments.html', {'appointments': appointments})


# def index(request):
#     #     json_serializer = serializers.get_serializer("json")()
#     #     appointments = json_serializer.serialize(
#     #         Appointment.objects.all(), ensure_ascii=False)
#     #    # appointments = Appointment.objects.all()
#     #     # context = {
#     #     #     'appointments': appointments
#     #     # }
#     appointments = Appointment.objects.all()
#     return render(request, 'appointments/appointments.html', {'appointments': appointments})


def delete_appointment(request, id):
    username = request.user.username
    user = StaffAccount.objects.get(email=username)
    userID = user.auth_id.id
    userlogin = StaffAuth.objects.get(username=username)
    if request.method == 'POST':
        print(request.POST, id)
        appointment = Appointment.objects.get(id=id)
        student = StudentAccount.objects.get(id=appointment.student_id.id)
        appointment.delete()
        student.delete()
        # appointments = Appointment.objects.all()
        appointments = Appointment.objects.filter(
            staff_id=userID)
        message = Mail(
            from_email='mobeenraza39@gmail.com',
            to_emails=student.email,
            subject='Your appointment for ' +
            str(appointment.start_date) + " is cancelled.",
            html_content="This is your confirmation email for the cancellation of your appointment.")
        try:
            sg = SendGridAPIClient(
                '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')
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)
        messages.success(
            request, 'Your appointment has been cancelled.')
        return redirect('/appointments/')
        # return render(request, 'appointments/appointments.html', {'appointments': appointments})


def edit_appointment(request, id):
    username = request.user.username
    user = StaffAccount.objects.get(email=username)
    userID = user.auth_id.id
    print(userID)
    userlogin = StaffAuth.objects.get(username=username)
    if request.method == 'POST':
        reason = ""
        appointment = Appointment.objects.get(id=id)
        if request.POST.get('fname'):
            reason = "Your first name for the appointment was updated to " + \
                request.POST.get('fname')
            StudentAccount.objects.filter(id=appointment.student_id.id).update(
                fname=request.POST.get('fname')
            )
        if request.POST.get('lname'):
            reason = "Your last name for the appointment was updated to " + \
                request.POST.get('lname')
            StudentAccount.objects.filter(id=appointment.student_id.id).update(
                lname=request.POST.get('lname')
            )
        if request.POST.get('studentnumber'):
            reason = "Your student number for the appointment was updated to " + \
                request.POST.get('studentnumber')
            StudentAccount.objects.filter(id=appointment.student_id.id).update(
                student_number=request.POST.get('studentnumber')
            )
        if request.POST.get('email'):
            reason = "Your email was updated to " + request.POST.get('email')
            StudentAccount.objects.filter(id=appointment.student_id.id).update(
                email=request.POST.get('email')
            )
        if request.POST.get('title'):
            reason = "Your appointment reason was updated to " + \
                request.POST.get('title')
            Appointment.objects.filter(id=id).update(
                title=request.POST.get('title')
            )
        if request.POST.get('start_date'):
            start_date = parser.parse(
                request.POST.get('start_date')).timestamp()
            for each in Appointment.objects.all():
                if start_date >= each.start_date.timestamp() and start_date <= each.end_date.timestamp():
                    messages.error(
                        request, 'Appointment for this date is already booked.')
                    return redirect('/appointments/')
            reason = "Your appointment start time was updated to " + \
                request.POST.get('start_date')
            Appointment.objects.filter(id=id).update(
                start_date=request.POST.get('start_date')
            )
        if request.POST.get('end_date'):
            end_date = parser.parse(request.POST.get('end_date')).timestamp()
            for each in Appointment.objects.all():
                if end_date >= each.start_date.timestamp() and end_date <= each.end_date.timestamp():
                    messages.error(
                        request, 'Appointment for this date is already booked.')
                    return redirect('/appointments/')
            reason = "Your appointment ending time was updated to " + \
                request.POST.get('end_date')
            Appointment.objects.filter(id=id).update(
                end_date=request.POST.get('end_date')
            )
        if request.POST.get('description'):
            reason = "The notes for your appointment were updated to " + \
                request.POST.get('description')
            Appointment.objects.filter(id=id).update(
                description=request.POST.get('description')
            )
        # appointments = Appointment.objects.all()
        appointments = Appointment.objects.filter(
            staff_id=userID)
        message = Mail(
            from_email='mobeenraza39@gmail.com',
            to_emails=str(appointment.student_id.email),
            subject=reason,
            html_content="This is your confirmation email for updating of your appointment.")
        try:
            sg = SendGridAPIClient(
                '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')
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)
        messages.success(
            request, 'Your appointment has been updated.')
        return redirect('/appointments/')


def appointment(request):
    return render(request, 'appointments/appointment.html')
