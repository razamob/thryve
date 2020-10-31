from rest_framework import serializers
from .models import StudentData

class StudentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentData
        fields = fields = ('fname',
        'lname',
        'email',
        'student_number',
        'phone_number',
        'program_year',
        'als',
        'coop',
        'international',
        'program_id_id',
        'auth_id_id')