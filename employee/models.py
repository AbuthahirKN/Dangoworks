from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id=models.IntegerField(primary_key=True)
    emp_name=models.CharField(max_length=40)
    email=models.EmailField()
    phone_number=models.CharField(max_length=40)
    designation=models.CharField(max_length=40)
    salary=models.IntegerField()
    Image=models.ImageField(upload_to='employee')
