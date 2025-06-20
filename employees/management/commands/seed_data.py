from django.core.management.base import BaseCommand
from faker import Faker
import random
from employees.models import Employee, Department
from attendance.models import Attendance
from performance.models import Performance

class Command(BaseCommand):
    help = "Seed the database with fake employees, attendance, and performance data"

    def add_arguments(self, parser):
        parser.add_argument('--employees', type=int, default=20, help='Number of employees to create')
        parser.add_argument('--attendance_per_employee', type=int, default=10, help='Number of attendance records per employee')
        parser.add_argument('--performance_records', type=int, default=50, help='Number of performance records total')

    def handle(self, *args, **options):
        fake = Faker()

        # --- Departments ---
        if Department.objects.count() == 0:
            departments = ['HR', 'IT', 'Finance', 'Marketing']
            for dept in departments:
                Department.objects.create(name=dept)
            self.stdout.write(self.style.SUCCESS('Default departments created.'))

        departments = list(Department.objects.all())

        # --- Employees ---
        employees = []
        for _ in range(options['employees']):
            emp = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone=fake.phone_number()[:10],
                address=fake.address(),
                date_of_joining=fake.date_between(start_date='-5y', end_date='today'),
                department=random.choice(departments)
            )
            employees.append(emp)

        self.stdout.write(self.style.SUCCESS(f'{options["employees"]} employees created.'))

        # --- Attendance ---
        statuses = ['present', 'absent', 'late']
        for employee in employees:
            for _ in range(options['attendance_per_employee']):
                Attendance.objects.create(
                    employee=employee,
                    date=fake.date_between(start_date='-30d', end_date='today'),
                    status=random.choice(statuses)
                )

        self.stdout.write(self.style.SUCCESS(f'Attendance data created for each employee.'))

        # --- Performance ---
        for _ in range(options['performance_records']):
            Performance.objects.create(
                employee=random.choice(employees),
                rating=random.randint(1, 5),
                review_date=fake.date_between(start_date='-1y', end_date='today')
            )

        self.stdout.write(self.style.SUCCESS(f'{options["performance_records"]} performance records created.'))
