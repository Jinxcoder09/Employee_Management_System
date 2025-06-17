from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import AttendanceSerializer
from employees.models import  Department, Performance
from .models import Attendance

from django.db.models import Count, Avg
def dashboard(request):
    # Example: Count of employees per department
    dept_counts = Department.objects.annotate(count=Count('employee'))
    
    # Example: Average performance scores
    avg_scores = Performance.objects.values('employee__department__name').annotate(avg_score=Avg('score'))

    context = {
        'dept_counts': list(dept_counts.values('name', 'count')),
        'avg_scores': list(avg_scores),
    }
    return render(request, 'dashboard.html', context)

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filterset_fields = ['date', 'status', 'employee']
