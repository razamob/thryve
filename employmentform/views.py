from django.shortcuts import render
from .models import EmploymentConsultantForm
from rest_framework.renderers import TemplateHTMLRenderer
from django.core import serializers
from rest_framework import viewsets
from .serializers import EmploymentConsultantFormSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


class EmploymentConsultantFormView(viewsets.ModelViewSet):
    serializer_class = EmploymentConsultantFormSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'employmentconsultantforms/employmentconsultantforms.html'
    queryset = EmploymentConsultantForm.objects.all()

    def list(self, request):
        queryset = EmploymentConsultantForm.objects.all().values()
        # studentauths = [
        #     studentauth.title for studentauth in StudentAuth.objects.all()]
        return JsonResponse({'employmentconsultantforms': list(queryset)})

    def create(self, request):
        print(request.POST)
        employmentconsultantform = EmploymentConsultantForm.objects.create(
            q1e_sso=request.POST.get('q1e_sso'),
            q1e_friend=request.POST.get('q1e_friend'),
            q1e_faculty=request.POST.get('q1e_faculty'),
            q1e_visit=request.POST.get('q1e_visit'),
            q1e_orient=request.POST.get('q1e_orient'),
            q1e_event=request.POST.get('q1e_event'),
            q1e_kpi2=request.POST.get('q1e_kpi2'),
            q1e_outreach=request.POST.get('q1e_outreach'),
            q1e_posters=request.POST.get('q1e_posters'),
            q1e_stv=request.POST.get('q1e_stv'),
            q1e_social=request.POST.get('q1e_social'),
            q1e_media=request.POST.get('q1e_media'),
            q1e_walkby=request.POST.get('q1e_walkby'),
            q1e_website=request.POST.get('q1e_website'),
            ecs_resume=request.POST.get('ecs_resume'),
            ecs_cover=request.POST.get('ecs_cover'),
            ecs_interview=request.POST.get('ecs_interview'),
            ecs_jobsearch=request.POST.get('ecs_jobsearch'),
            ecs_mockinterview=request.POST.get('ecs_mockinterview'),
            ecs_networking=request.POST.get('ecs_networking'),
            ecs_portfolio=request.POST.get('ecs_portfolio')
        )
        serializer = EmploymentConsultantFormSerializer(employmentconsultantform)
        employmentconsultantforms = EmploymentConsultantForm.objects.filter(id=employmentconsultantform.id).values()
        # return render(request, 'studentauths/studentauths.html', {'studentauths': studentauths})
        return JsonResponse({'employmentconsultantforms': list(employmentconsultantforms)})

    # def destroy(self, request, pk):
    #     studentauth = StudentAuth.objects.get(id=pk)
    #     studentauth.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class EmploymentConsultantFormAPI(viewsets.ModelViewSet):
    queryset = EmploymentConsultantForm.objects.all()
    serializer_class = EmploymentConsultantFormSerializer


def index(request):
    #     json_serializer = serializers.get_serializer("json")()
    #     appointments = json_serializer.serialize(
    #         Appointment.objects.all(), ensure_ascii=False)
    #    # appointments = Appointment.objects.all()
    #     # context = {
    #     #     'appointments': appointments
    #     # }
    employmentconsultantforms = EmploymentConsultantForm.objects.all()
    return JsonResponse(request, 'employmentconsultantforms/employmentconsultantforms.html', {'employmentconsultantforms': employmentconsultantforms})


def delete_employmentconsultantform(request, id):
    if request.method == 'POST':
        print(request.POST, id)
        employmentconsultantform = EmploymentConsultantForm.objects.get(id=id)
        employmentconsultantform.delete()
        employmentconsultantforms = EmploymentConsultantForm.objects.all()
        return render(request, 'employmentconsultantforms/employmentconsultantforms.html', {'employmentconsultantforms': employmentconsultantforms})

@csrf_exempt
def insert_employmentconsultantform(request):
    received_json_data = json.loads(request.body.decode("utf-8"))
    employmentconsultantform = EmploymentConsultantForm.objects.create(
        q1e_sso=received_json_data['q1e_sso'],
        q1e_friend=received_json_data['q1e_friend'],
        q1e_faculty=received_json_data['q1e_faculty'],
        q1e_visit=received_json_data['q1e_visit'],
        q1e_orient=received_json_data['q1e_orient'],
        q1e_event=received_json_data['q1e_event'],
        q1e_kpi2=received_json_data['q1e_kpi2'],
        q1e_outreach=received_json_data['q1e_outreach'],
        q1e_posters=received_json_data['q1e_posters'],
        q1e_stv=received_json_data['q1e_stv'],
        q1e_social=received_json_data['q1e_social'],
        q1e_media=received_json_data['q1e_media'],
        q1e_walkby=received_json_data['q1e_walkby'],
        q1e_website=received_json_data['q1e_website'],
        ecs_resume=received_json_data['ecs_resume'],
        ecs_cover=received_json_data['ecs_cover'],
        ecs_interview=received_json_data['ecs_interview'],
        ecs_jobsearch=received_json_data['ecs_jobsearch'],
        ecs_mockinterview=received_json_data['ecs_mockinterview'],
        ecs_networking=received_json_data['ecs_networking'],
        ecs_portfolio=received_json_data['ecs_portfolio']
    )
    serializer = EmploymentConsultantFormSerializer(employmentconsultantform)
    employmentconsultantforms = EmploymentConsultantForm.objects.filter(id=employmentconsultantform.id).values()
    return JsonResponse({"employmentconsultantforms": list(employmentconsultantforms)})

#def edit_studentauth(request, id):
#    if request.method == 'POST':
#        if request.POST.get('sheridan_id'):
#            StudentAuth.objects.filter(id=id).update(
#                sheridan_id=request.POST.get('sheridan_id')
#            )
#        if request.POST.get('password'):
#            StudentAuth.objects.filter(id=id).update(
#                password=request.POST.get('password')
#            )
#        studentauths = StudentAuth.objects.all()
#        return render(request, 'studentauths/studentauths.html', {'studentauths': studentauths})


def studentauth(request):
    return render(request, 'employmentconsultantforms/employmentconsultantform.html')

# Create your views here.
