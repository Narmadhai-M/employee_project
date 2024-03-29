# Generated by Django 5.0 on 2023-12-30 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0006_remove_employee_email_remove_employee_emp_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(default='N/A', max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='username',
            field=models.CharField(default='N/A', max_length=20, unique=True),
        ),
    ]
