from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    emp_id=models.CharField(unique=True,max_length=15)
    emp_name=models.CharField(max_length=70)
    emp_sal=models.FloatField()
    emp_addr=models.CharField(max_length=200)
