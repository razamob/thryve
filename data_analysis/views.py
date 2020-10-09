from django.http import JsonResponse
from django.shortcuts import render
from data_analysis.models import School
from django.core import serializers


def data_dashboard(request):
    return render(request, 'data_analysis/data_dashboard.html')


def staff_data(request):
    dataset = School.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)
