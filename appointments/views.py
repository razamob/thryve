from django.shortcuts import render
from .models import Appointment
from rest_framework.renderers import TemplateHTMLRenderer
from django.core import serializers
from rest_framework import viewsets
from .serializers import AppointmentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
import json
from django.http import JsonResponse


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
        print(request.POST)
        appointment = Appointment.objects.create(
            title=request.POST.get('title'),
            start_date=request.POST.get('start_date'),
            end_date=request.POST.get('end_date'),
            description=request.POST.get('description')
        )
        serializer = AppointmentSerializer(appointment)
        appointments = Appointment.objects.all()
        #return render(request, 'appointments/appointments.html', {'appointments': appointments})
        return JsonResponse(appointment)

    # def destroy(self, request, pk):
    #     appointment = Appointment.objects.get(id=pk)
    #     appointment.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class AppointmentAPI(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


def index(request):
    #     json_serializer = serializers.get_serializer("json")()
    #     appointments = json_serializer.serialize(
    #         Appointment.objects.all(), ensure_ascii=False)
    #    # appointments = Appointment.objects.all()
    #     # context = {
    #     #     'appointments': appointments
    #     # }
    appointments = Appointment.objects.all()
    return render(request, 'appointments/appointments.html', {'appointments': appointments})


def delete_appointment(request, id):
    if request.method == 'POST':
        print(request.POST, id)
        appointment = Appointment.objects.get(id=id)
        appointment.delete()
        appointments = Appointment.objects.all()
        return render(request, 'appointments/appointments.html', {'appointments': appointments})


def edit_appointment(request, id):
    if request.method == 'POST':
        if request.POST.get('title'):
            Appointment.objects.filter(id=id).update(
                title=request.POST.get('title')
            )
        if request.POST.get('start_date'):
            Appointment.objects.filter(id=id).update(
                start_date=request.POST.get('start_date')
            )
        if request.POST.get('end_date'):
            Appointment.objects.filter(id=id).update(
                end_date=request.POST.get('end_date')
            )
        if request.POST.get('description'):
            Appointment.objects.filter(id=id).update(
                description=request.POST.get('description')
            )
        appointments = Appointment.objects.all()
        return render(request, 'appointments/appointments.html', {'appointments': appointments})


def appointment(request):
    return render(request, 'appointments/appointment.html')
