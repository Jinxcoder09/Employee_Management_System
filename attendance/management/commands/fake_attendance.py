from django.core.management.base import BaseCommand
from attendance.models import Attendance
from employees.models import Employee
from faker import Faker
import random

class Command(BaseCommand):
    help = "Insert fake attendance data"

    def handle(self, *args, **kwargs):
        fake = Faker()
        statuses = ['present', 'absent', 'late']
        employees = Employee.objects.all()

        if not employees.exists():
            self.stdout.write(self.style.ERROR('No employees found. Add employees first.'))
            return

        for employee in employees:
            for _ in range(10):  # Generate 10 days of attendance for each employee
                Attendance.objects.create(
                    employee=employee,
                    date=fake.date_between(start_date='-30d', end_date='today'),
                    status=random.choice(statuses)
                )
        self.stdout.write(self.style.SUCCESS('Fake attendance data inserted successfully!'))
