# Generated by Django 5.0 on 2023-12-30 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='title',
            field=models.CharField(choices=[('IT', 'Information Technology'), ('HR', 'Human Resources'), ('Sales', 'Sales'), ('Marketing', 'Marketing')], max_length=20),
        ),
    ]