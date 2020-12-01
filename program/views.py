from django.shortcuts import render
from .models import SchoolProgram
from rest_framework.renderers import TemplateHTMLRenderer
from django.core import serializers
from rest_framework import viewsets
from .serializers import SchoolProgramSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
import json
from django.http import JsonResponse


class SchoolProgramView(viewsets.ModelViewSet):
    serializer_class = SchoolProgramSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'schoolprograms/schoolprograms.html'
    queryset = SchoolProgram.objects.all()

    def list(self, request):
        queryset = SchoolProgram.objects.all().values()
        return JsonResponse({'schoolprograms': list(queryset)})

    def create(self, request):
        print(request.POST)
        schoolprogram = SchoolProgram.objects.create(
            program_code=request.POST.get('program_code'),
            program_title=request.POST.get('program_title'),
            faculty_code=request.POST.get('faculty_code'),
            educ_level=request.POST.get('educ_level')
        )
        serializer = SchoolProgramSerializer(schoolprogram)
        schoolprograms = SchoolProgram.objects.filter(id=schoolprogram.id).values()
        return JsonResponse({'schoolprograms': list(schoolprograms)})

class SchoolProgramAPI(viewsets.ModelViewSet):
    queryset = SchoolProgram.objects.all()
    serializer_class = SchoolProgramSerializer


def index(request):
    schoolprograms = SchoolProgram.objects.all()
    return JsonResponse(request, 'schoolprograms/schoolprograms.html', {'schoolprograms': schoolprograms})

def find_schoolprogram(request, id):
    schoolprogram = SchoolProgram.objects.filter(id=id).values()
    return JsonResponse({"schoolprogram": list(schoolprogram)})

def schoolprogram(request):
    return render(request, 'schoolprograms/schoolprograms.html')

# Create your views here.
