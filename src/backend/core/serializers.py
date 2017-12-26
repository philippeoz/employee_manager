from backend.core.models.employee import Employee

from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'name',
            'email',
            'department'
        ]
