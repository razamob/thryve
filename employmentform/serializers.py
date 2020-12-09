from rest_framework import serializers
from employmentform.models import EmploymentConsultantForm

class EmploymentConsultantFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentConsultantForm
        fields = ('q1e_sso',
        'q1e_friend',
        'q1e_faculty',
        'q1e_visit',
        'q1e_orient',
        'q1e_event',
        'q1e_kpi2',
        'q1e_outreach',
        'q1e_posters',
        'q1e_stv',
        'q1e_social',
        'q1e_media',
        'q1e_walkby',
        'q1e_website',
        'ecs_resume',
        'ecs_cover',
        'ecs_interview',
        'ecs_jobsearch',
        'ecs_mockinterview',
        'ecs_networking',
        'ecs_portfolio',)