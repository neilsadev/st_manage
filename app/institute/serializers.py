from rest_framework import serializers
from .models import Institute

# class Bser(sre):
#     S

class InstituteSerializer(serializers.ModelSerializer):
    # b=Bser()
    class Meta:
        model = Institute
        fields = ['id', 'name', 'uuid', 'year', 'address', 'created_at', 'updated_at']