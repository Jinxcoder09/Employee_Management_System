from django.core.management.base import BaseCommand
from employees.models import Employee, Department
from faker import Faker
import random

class Command(BaseCommand):
    help = "Seed the database with fake employee data"

    def add_arguments(self, parser):
        parser.add_argument('--total', type=int, help='Number of employees to create')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker()

        # Make sure at least one department exists
        if Department.objects.count() == 0:
            departments = ['HR', 'IT', 'Finance', 'Marketing']
            for dept in departments:
                Department.objects.create(name=dept)

        departments = list(Department.objects.all())

        for _ in range(total):
            Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone=fake.phone_number()[:10],
                address=fake.address(),
                date_of_joining=fake.date_between(start_date='-5y', end_date='today'),
                department=random.choice(departments)
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully added {total} employees'))
