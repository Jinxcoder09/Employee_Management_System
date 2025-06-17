# employee_project/views.py

from django.shortcuts import render
from django.db.models import Count, Avg, Sum
from django.db.models.functions import ExtractMonth, ExtractYear # Essential for monthly grouping

from employees.models import Employee
from attendance.models import Attendance
from performance.models import Performance

import calendar # To get month names for labels
import json # <--- ADD THIS LINE

def dashboard(request):
    print("--- Dashboard View Called ---")

    # 1. Department-wise employee count (for Pie Chart)
    dept_summary = Employee.objects.values('department__name').annotate(emp_count=Count('id'))
    dept_labels = [item['department__name'] for item in dept_summary]
    dept_counts = [item['emp_count'] for item in dept_summary]
    print(f"Department Summary: {dept_summary}")
    print(f"Dept Labels: {dept_labels}")
    print(f"Dept Counts: {dept_counts}")

    # 2. Average performance per department (Bar Chart)
    perf_summary = Performance.objects.values('employee__department__name').annotate(avg_rating=Avg('rating'))
    perf_labels = [item['employee__department__name'] for item in perf_summary]
    perf_scores = [item['avg_rating'] if item['avg_rating'] is not None else 0 for item in perf_summary]
    print(f"Performance Summary: {perf_summary}")
    print(f"Perf Labels: {perf_labels}")
    print(f"Perf Scores: {perf_scores}")

    # 3. Top 5 attendance by recorded days (Bar Chart)
    attendance_summary = Attendance.objects.values('employee__name').annotate(days_recorded=Count('id')).order_by('-days_recorded')[:5]
    att_labels = [item['employee__name'] for item in attendance_summary]
    att_counts = [item['days_recorded'] for item in attendance_summary]
    print(f"Attendance Summary: {attendance_summary}")
    print(f"Att Labels: {att_labels}")
    print(f"Att Counts: {att_counts}")

    # 4. Monthly Attendance Overview (NEW BAR CHART DATA)
    monthly_att_summary = Attendance.objects.annotate(
        year=ExtractYear('date'),
        month=ExtractMonth('date')
    ).values('year', 'month').annotate(
        total_attendance=Count('id')
    ).order_by('year', 'month')

    monthly_att_labels = []
    monthly_att_counts = []
    for item in monthly_att_summary:
        month_name = calendar.month_abbr[item['month']]
        monthly_att_labels.append(f"{month_name} {item['year']}")
        monthly_att_counts.append(item['total_attendance'])

    print(f"Monthly Attendance Summary QuerySet: {monthly_att_summary}")
    print(f"Monthly Attendance Labels: {monthly_att_labels}")
    print(f"Monthly Attendance Counts: {monthly_att_counts}")

    # Prepare context dictionary to pass data to the template
    context = {
        'dept_labels_json': json.dumps(dept_labels), # <--- USE json.dumps()
        'dept_counts_json': json.dumps(dept_counts), # <--- USE json.dumps()
        'perf_labels_json': json.dumps(perf_labels), # <--- USE json.dumps()
        'perf_scores_json': json.dumps(perf_scores), # <--- USE json.dumps()
        'att_labels_json': json.dumps(att_labels),   # <--- USE json.dumps()
        'att_counts_json': json.dumps(att_counts),   # <--- USE json.dumps()
        'monthly_att_labels_json': json.dumps(monthly_att_labels), # <--- USE json.dumps()
        'monthly_att_counts_json': json.dumps(monthly_att_counts), # <--- USE json.dumps()
    }
    print(f"Final Context Passed to Template: {context}")
    print("--- Dashboard View Finished ---")

    return render(request, 'dashboard.html', context)