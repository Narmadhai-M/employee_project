# Generated by Django 5.0 on 2024-01-01 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0008_alter_employee_email_alter_employee_emp_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_code',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]