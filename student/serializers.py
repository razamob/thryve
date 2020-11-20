from rest_framework import serializers
from student.models import StudentAccount

class StudentAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAccount
        fields = ('fname',
        'lname',
        'email',
        'student_number',
        'phone_number',
        'program_year',
        'als',
        'coop',
        'international',
        'program_id',
        'auth_id')