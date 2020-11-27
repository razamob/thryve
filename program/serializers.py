from rest_framework import serializers
from .models import SchoolProgram

class SchoolProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolProgram
        fields = ('program_code', 'program_title', 'faculty_code', 'educ_level')