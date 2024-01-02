# Generated by Django 5.0 on 2023-12-30 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0004_alter_employee_mobile_alter_position_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Position',
            new_name='Department',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='position',
            new_name='dept',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='emp_code',
        ),
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(default='N/A', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='N/A', max_length=4),
        ),
        migrations.AddField(
            model_name='employee',
            name='username',
            field=models.CharField(default='N/A', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='mobile',
            field=models.CharField(default='N/A', max_length=15),
        ),
    ]
