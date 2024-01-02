from django.shortcuts import render,redirect
from requests import request

from employee_register.models import Employee
from .forms import EmployeeForm
from django.core.exceptions import ValidationError
from validate_email_address import validate_email

# Create your views here.
def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)

def employee_form(request,id=0):
     if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form})
     else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            # verify email number is already present 
            username = form.cleaned_data['username']
            if Employee.objects.exclude(pk=id).filter(username=username).exists():
                if 'username' not in form._errors:
                    form.add_error('username', 'This username is already taken. Please choose a different one.')
                form._errors['username'] = form.error_class()

             # verify email number is already present 
            email = form.cleaned_data['email']
            if Employee.objects.exclude(pk=id).filter(email=email).exists():
                if 'email' not in form._errors:
                    form.add_error('email', 'This email is already registered. Please use a different one.')
                form._errors['email'] = form.error_class()

            # verify mobile number is already present
            mobile = form.cleaned_data['mobile']
            if Employee.objects.exclude(pk=id).filter(mobile=mobile).exists():
                if 'mobile' not in form._errors:
                    form.add_error('mobile', 'This mobile number is already registered. Please use a different one.')
                form._errors['mobile'] = form.error_class()

             # verify emp_id number is already present
            emp_code = form.cleaned_data['emp_code']
            if Employee.objects.exclude(pk=id).filter(emp_code=emp_code).exists():
                if 'emp_code' not in form._errors:
                    form.add_error('emp_code', 'This employee code is already registered. Please use a different one.')
                form._errors['emp_code'] = form.error_class()

            # Save the form if  no errors
            if not any(form.errors):
                form.save()
                return redirect('/employee/list')

        return render(request, "employee_register/employee_form.html", {'form': form})
def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')