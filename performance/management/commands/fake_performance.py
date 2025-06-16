from django.core.management.base import BaseCommand
from faker import Faker
import random
from performance.models import Performance
from employees.models import Employee

class Command(BaseCommand):
    help = 'Generate fake Performance data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        employees = Employee.objects.all()

        if not employees.exists():
            self.stdout.write("No employees found. Add employees first.")
            return

        for _ in range(50):  # how many fake records you want
            employee = random.choice(employees)
            rating = random.randint(1, 5)  # assuming rating scale 1-5
            review_date = fake.date_between(start_date='-1y', end_date='today')

            Performance.objects.create(
                employee=employee,
                rating=rating,
                review_date=review_date
            )

        self.stdout.write(self.style.SUCCESS('Successfully added 50 fake Performance records.'))
