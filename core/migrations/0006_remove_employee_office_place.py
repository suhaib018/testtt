# Generated by Django 4.0.3 on 2022-03-29 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_department_office_place_employee_office_place'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='office_place',
        ),
    ]
