from django.shortcuts import render
from employees.models import Department, Performance
from django.db.models import Count, Avg

def dashboard(request):
    # Employees per department
    dept_counts = (
        Department.objects
        .annotate(count=Count('employee'))
        .values('name', 'count')
    )

    # Avg performance score per department
    avg_scores = (
        Performance.objects
        .values('employee__department__name')
        .annotate(avg_score=Avg('score'))
    )

    return render(request, 'dashboard.html', {
        'dept_counts': list(dept_counts),   # convert to list for JSON serialization
        'avg_scores': list(avg_scores),
    })
