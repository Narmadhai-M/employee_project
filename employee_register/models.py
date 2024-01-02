from django.db import models

# Create your models here.
class Department(models.Model):
    IT_DEPARTMENT = 'IT'
    HR_DEPARTMENT = 'HR'
    CMS_DEPARTMENT = "CMS"
    MARKETING_DEPARTMENT = 'Marketing'
    FINANCE_DEPARTMENT ="Finance"
    DEPARTMENT_CHOICES = [
        (IT_DEPARTMENT, 'Information Technology'),
        (HR_DEPARTMENT, 'Human Resources'),
        (MARKETING_DEPARTMENT, 'Marketing'),
        (CMS_DEPARTMENT,'CMS'),
        (FINANCE_DEPARTMENT,'Finance'),
    ]
   
    title=models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    def __str__(self):
        return self.title
class Employee(models.Model):
    username=models.CharField(max_length=20,unique=True,)
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=4)
    email=models.EmailField(max_length=50,unique=True)
    mobile = models.CharField(max_length=10,unique=True)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE)