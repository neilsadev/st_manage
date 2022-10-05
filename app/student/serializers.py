from rest_framework import serializers
from .models import *
from institute.models import Department
from institute.serializers import DepartmentSerializer

class StudentSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(queryset = Department.objects.all(), many=False)
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'uuid', 'department', 'email', 'phone', 'birthyear', 'address', 'created_at', 'updated_at']
