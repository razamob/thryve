from django.shortcuts import render
from student.models import StudentAccount
from studentauth.models import StudentAuth
from program.models import SchoolProgram
from rest_framework.renderers import TemplateHTMLRenderer
from django.core import serializers
from rest_framework import viewsets
from .serializers import StudentAccountSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


class StudentAccountView(viewsets.ModelViewSet):
    serializer_class = StudentAccountSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'studentaccounts/studentaccounts.html'
    queryset = StudentAccount.objects.all()

    serializer_class = StudentAccountSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'studentaccounts/studentaccounts.html'
    queryset = StudentAccount.objects.all()

    def list(self, request):
        queryset = StudentAccount.objects.all().values()
        # student = [
        #     student.title for student in Student.objects.all()]
        return JsonResponse({"studentaccounts": list(queryset)})

    def create(self, request):
        print(request.POST)
        id_prog = request.POST.get('program_id')
        new_prog = SchoolProgram.objects.get(id=id_prog)

        id_auth = request.POST.get('auth_id')
        new_auth = StudentAuth.objects.get(id=id_auth)

        studentaccount = StudentAccount.objects.create(
            fname=request.POST.get('fname'),
            lname=request.POST.get('lname'),
            email=request.POST.get('email'),
            student_number=request.POST.get('student_number'),
            program_year=request.POST.get('program_year'),
            als=request.POST.get('als'),
            coop=request.POST.get('coop'),
            international=request.POST.get('international'),
            program_id=new_prog,
            auth_id=new_auth,
            phone_number=request.POST.get('phone number')
        )
        serializer = StudentAccountSerializer(studentaccount)
        studentaccounts = StudentAccount.objects.filter(
            id=studentaccount.id).values()
        return JsonResponse({"studentaccounts": list(studentaccounts)})

    # def destroy(self, request, pk):
    #     studentaccount = StudentAccount.objects.get(id=pk)
    #     studentaccount.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class StudentAccountAPI(viewsets.ModelViewSet):
    queryset = StudentAccount.objects.all()
    serializer_class = StudentAccountSerializer


def index(request):
    #     json_serializer = serializers.get_serializer("json")()
    #     appointments = json_serializer.serialize(
    #         Appointment.objects.all(), ensure_ascii=False)
    #    # appointments = Appointment.objects.all()
    #     # context = {
    #     #     'appointments': appointments
    studentaccounts = StudentAccount.objects.all()
    return JsonResponse(request, 'studentaccounts/studentaccounts.html', {'studentaccounts': studentaccounts})


@csrf_exempt
def insert_studentaccount(request, auth, prog):
    new_auth = StudentAuth.objects.get(id=auth)
    print(new_auth)
    new_prog = SchoolProgram.objects.get(id=prog)
    print(new_prog)
    received_json_data = json.loads(request.body.decode("utf-8"))
    studentaccount = StudentAccount.objects.create(
        fname=received_json_data['fname'],
        lname=received_json_data['lname'],
        email=received_json_data['email'],
        student_number=received_json_data['student_number'],
        program_year=received_json_data['program_year'],
        als=received_json_data['als'],
        coop=received_json_data['coop'],
        gpa=received_json_data['gpa'],
        education_level=received_json_data['education_level'],
        international=received_json_data['international'],
        student_status=received_json_data['student_status'],
        program_id=new_prog,
        auth_id=new_auth,
        phone_number=received_json_data['phone_number']
    )
    serializer = StudentAccountSerializer(studentaccount)
    studentaccounts = StudentAccount.objects.filter(
        id=studentaccount.id).values()
    return JsonResponse({"studentaccounts": list(studentaccounts)})


def find_studentaccount(request, id):
    studentaccount = StudentAccount.objects.filter(id=id).values()
    return JsonResponse({"studentaccount": list(studentaccount)})


def delete_studentaccount(request, id):
    if request.method == 'POST':
        print(request.POST, id)
        studentaccount = StudentAccount.objects.get(id=id)
        studentaccount.delete()
        studentaccounts = StudentAccount.objects.all().values()
        return JsonResponse(request, 'studentaccounts/studentaccounts.html', {'studentaccounts': studentaccounts})


def edit_studentaccount(request, id):
    if request.method == 'POST':
        if request.POST.get('fname'):
            StudentAccount.objects.filter(id=id).update(
                fname=request.POST.get('fname')
            )
        if request.POST.get('lname'):
            StudentAccount.objects.filter(id=id).update(
                lname=request.POST.get('lname')
            )
        if request.POST.get('email'):
            StudentAccount.objects.filter(id=id).update(
                email=request.POST.get('email')
            )
        if request.POST.get('student_number'):
            StudentAccount.objects.filter(id=id).update(
                student_number=request.POST.get('student_number')
            )
        if request.POST.get('phone_number'):
            StudentAccount.objects.filter(id=id).update(
                phone_number=request.POST.get('phone_number')
            )
        if request.POST.get('program_year'):
            StudentAccount.objects.filter(id=id).update(
                program_year=request.POST.get('program_year')
            )
        if request.POST.get('als'):
            StudentAccount.objects.filter(id=id).update(
                als=request.POST.get('als')
            )
        if request.POST.get('coop'):
            StudentAccount.objects.filter(id=id).update(
                coop=request.POST.get('coop')
            )
        if request.POST.get('international'):
            StudentAccount.objects.filter(id=id).update(
                international=request.POST.get('international')
            )
        if request.POST.get('program_id'):
            StudentAccount.objects.filter(id=id).update(
                program_id=request.POST.get('program_id')
            )
        if request.POST.get('auth_id'):
            StudentAccount.objects.filter(id=id).update(
                auth_id=request.POST.get('auth_id')
            )
        studentaccounts = StudentAccount.objects.filter(id=id).values()
        return render(request, 'studentaccounts/studentaccounts.html', {'studentaccounts': studentaccounts})


def studentaccount(request):
    return render(request, 'studentaccounts/studentaccount.html')
