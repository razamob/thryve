from django.shortcuts import render
from .models import StudentData
from rest_framework.renderers import TemplateHTMLRenderer
from django.core import serializers
from rest_framework import viewsets
from .serializers import StudentDataSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
import json
from django.http import JsonResponse

# Create your views here.

class StudentDataView(viewsets.ModelViewSet):
    serializer_class = StudentDataSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'studentdatas/studentdatas.html'
    queryset = StudentData.objects.all()

    def list(self, request):
        queryset = StudentData.objects.all().values()
        return JsonResponse({"studentdatas": list(queryset)})

    def create(self, request):
        print(request.POST)
        studentdata = StudentData.objects.create(
            fname = request.POST.get('fname'),
            lname = request.POST.get('lname'),
            email = request.POST.get('email'),
            student_number = request.POST.get('student_number'),
            program_year = request.POST.get('program_year'),
            als = request.POST.get('als'),
            coop = request.POST.get('coop'),
            international = request.POST.get('international'),
            program_id = request.POST.get('program_id_id'),
            auth_id = request.POST.get('auth_id_id'),
            phone_number = request.POST.get('phone number')
        )
        serializer = StudentDataSerializer(studentdata)
        studentdata = StudentData.objects.last().values()
        return JsonResponse({"studentdatas": list(studentdata)})

    # def destroy(self, request, pk):
    #     appointment = Appointment.objects.get(id=pk)
    #     appointment.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class StudentDataAPI(viewsets.ModelViewSet):
    queryset = StudentData.objects.all()
    serializer_class = StudentDataSerializer


def index(request):
    studentdatas = StudentData.objects.all().values()
    return JsonResponse({"studentdatas": list(studentdatas)})


def delete_studentdata(request, id):
    if request.method == 'POST':
        print(request.POST, id)
        studentdata = StudentData.objects.get(id=id)
        studentdata.delete()
        studentdatas = StudentData.objects.all().values()
        return JsonResponse({"studentdatas": list(studentdatas)})


def edit_studentdata(request, id):
    if request.method == 'POST':
        if request.POST.get('fname'):
            StudentData.objects.filter(id=id).update(
                fname=request.POST.get('fname')
            )
        if request.POST.get('lname'):
            StudentData.objects.filter(id=id).update(
                lname=request.POST.get('lname')
            )
        if request.POST.get('email'):
            StudentData.objects.filter(id=id).update(
                email=request.POST.get('email')
            )
        if request.POST.get('student_number'):
            StudentData.objects.filter(id=id).update(
                student_number=request.POST.get('student_number')
            )
        if request.POST.get('phone_number'):
            StudentData.objects.filter(id=id).update(
                phone_number=request.POST.get('phone_number')
            )
        if request.POST.get('program_year'):
            StudentData.objects.filter(id=id).update(
                program_year=request.POST.get('program_year')
            )
        if request.POST.get('als'):
            StudentData.objects.filter(id=id).update(
                als=request.POST.get('als')
            )
        if request.POST.get('coop'):
            StudentData.objects.filter(id=id).update(
                coop=request.POST.get('coop')
            )
        if request.POST.get('international'):
            StudentData.objects.filter(id=id).update(
                international=request.POST.get('international')
            )
        if request.POST.get('program_id_id'):
            StudentData.objects.filter(id=id).update(
                program_id=request.POST.get('program_id_id')
            )
        if request.POST.get('auth_id_id'):
            StudentData.objects.filter(id=id).update(
                auth_id=request.POST.get('auth_id_id')
            )
        studentdatas = StudentData.objects.all().values()
        return JsonResponse({"studentdatas": list(studentdata)})


def studentdata(request):
    return render(request, 'studentdatas/studentdata.html')