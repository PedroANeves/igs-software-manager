from rest_framework import serializers

from .models import Employee

class EmployeeSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('name', 'email', 'departament')
