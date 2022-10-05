from rest_framework import serializers
from .models import Department, Institute

class InstituteSerializer(serializers.ModelSerializer):
    departments = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Institute
        fields = ['id', 'name', 'uuid', 'year', 'address', 'departments', 'created_at', 'updated_at']

class DepartmentSerializer(serializers.ModelSerializer):
    institute = serializers.PrimaryKeyRelatedField(queryset = Institute.objects.all(), many=False)
    class Meta:
        model = Department
        fields = ['id', 'name', 'degree', 'institute']
