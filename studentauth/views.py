from django.shortcuts import render
from .models import StudentAuth
from rest_framework.renderers import TemplateHTMLRenderer
from django.core import serializers
from rest_framework import viewsets
from .serializers import StudentAuthSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
import json
from django.http import JsonResponse


class StudentAuthView(viewsets.ModelViewSet):
    serializer_class = StudentAuthSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'studentauths/studentauths.html'
    queryset = StudentAuth.objects.all()

    def list(self, request):
        queryset = StudentAuth.objects.all().values()
        # studentauths = [
        #     studentauth.title for studentauth in StudentAuth.objects.all()]
        return JsonResponse({'studentauths': list(queryset)})

    def create(self, request):
        print(request.POST)
        studentauth = StudentAuth.objects.create(
            sheridan_id=request.POST.get('sheridan_id'),
            password=request.POST.get('password')
        )
        serializer = StudentAuthSerializer(studentauth)
        studentauths = StudentAuth.objects.filter(id=studentauth.id).values()
        # return render(request, 'studentauths/studentauths.html', {'studentauths': studentauths})
        return JsonResponse({'studentauths': list(studentauths)})

    # def destroy(self, request, pk):
    #     studentauth = StudentAuth.objects.get(id=pk)
    #     studentauth.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class StudentAuthAPI(viewsets.ModelViewSet):
    queryset = StudentAuth.objects.all()
    serializer_class = StudentAuthSerializer


def index(request):
    #     json_serializer = serializers.get_serializer("json")()
    #     appointments = json_serializer.serialize(
    #         Appointment.objects.all(), ensure_ascii=False)
    #    # appointments = Appointment.objects.all()
    #     # context = {
    #     #     'appointments': appointments
    #     # }
    studentauths = StudentAuth.objects.all()
    return JsonResponse(request, 'studentauths/studentauths.html', {'studentauths': studentauths})


def delete_studentauth(request, id):
    if request.method == 'POST':
        print(request.POST, id)
        studentauth = StudentAuth.objects.get(id=id)
        studentauth.delete()
        studentauths = StudentAuth.objects.all()
        return render(request, 'studentauths/studentauths.html', {'studentauths': studentauths})


def edit_studentauth(request, id):
    if request.method == 'POST':
        if request.POST.get('sheridan_id'):
            StudentAuth.objects.filter(id=id).update(
                sheridan_id=request.POST.get('sheridan_id')
            )
        if request.POST.get('password'):
            StudentAuth.objects.filter(id=id).update(
                password=request.POST.get('password')
            )
        studentauths = StudentAuth.objects.all()
        return render(request, 'studentauths/studentauths.html', {'studentauths': studentauths})


def studentauth(request):
    return render(request, 'studentauths/studentauth.html')

# Create your views here.
