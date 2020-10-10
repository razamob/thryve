from rest_framework import serializers
from .models import StudentAuth

class StudentAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAuth
        fields = ('sheridan_id',
        'password')