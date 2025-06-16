from django.db import models

# Department Model
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Employee Model
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    date_of_joining = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Attendance Model
class Attendance(models.Model):
    STATUS_CHOICES = (
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Leave', 'Leave'),
    )
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_attendances')
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.employee.name} - {self.date} - {self.status}"


# Performance Model
class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_performance')
    review_date = models.DateField()
    rating = models.IntegerField()  # 1 to 5 or 1 to 10 scale
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.employee.name} - {self.review_date} - Rating: {self.rating}"
