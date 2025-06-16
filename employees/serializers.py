from rest_framework import serializers
from .models import Employee, Department
from attendance.models import Attendance
from performance.models import Performance

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(), source='department', write_only=True
    )

    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'phone', 'address', 'date_of_joining', 'department', 'department_id']
