from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
 
 class Meta:
  model=Employee
  fields="__all__"
  labels={
   'fullname':'FULL NAME',
   'emp_code':'EMPLOYEE-ID',
   'username':'USERNAME',
   'email':'EMAIL-ID',
   'mobile':'MOBILE-ID',
   'dept':'DEPARTMENT-NAME',

   

  }
 