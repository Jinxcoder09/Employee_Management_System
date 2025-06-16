from django.db import models
from employees.models import Employee
# Create your models here.
class Performance(models.Model):
    employee= models.ForeignKey(Employee, on_delete=models.CASCADE)
    rating= models.IntegerField()
    review_date= models.DateField()
    def __str__(self):
        return f'{self.employee.name} - {self.rating}'