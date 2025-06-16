from django.db import models
from employees.models import Employee

# Create your models here.
class Attendance(models.Model):
    STATUS_CHOICES=[
        ('present', 'present'),
        ('absent', 'absent'),
        ('late', 'late'),
    ]
    employee=models.ForeignKey(Employee, on_delete= models.CASCADE)
    date=models.DateField()
    status= models.CharField(max_length=10, choices=STATUS_CHOICES)
    def __str__(self):
        return f"{self.employee.name} - {self.date} - {self.status}"