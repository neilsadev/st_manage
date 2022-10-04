from rest_framework import serializers
from .models import Department, Institute

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'degree']

class InstituteSerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(many = True,  required=False)
    class Meta:
        model = Institute
        fields = ['id', 'name', 'uuid', 'year', 'address', 'departments', 'created_at', 'updated_at']
