from faker import Faker
fake=Faker()
from random import *
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crudproject.settings')
import django
django.setup()
from testapp.models import EmployeeModel

def employees(n):
    for i in range(n):
        emp_id = 'EMP' + str(fake.unique.random_int(min=100000, max=999999))
        emp_name=fake.name()
        emp_sal=fake.random_int(min=10000, max=800000)
        emp_addr=fake.city()
        employee=EmployeeModel.objects.get_or_create(
        emp_id=emp_id,
        emp_name=emp_name,
        emp_sal=emp_sal,
        emp_addr=emp_addr
    )
n=int(input("Enter no.of Employee's should fill in the table:"))
employees(n)
print(f"{n} Records successfully inserted")

