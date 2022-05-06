from django.db import models
from versatileimagefield.fields import VersatileImageField, PPOIField


# Create your models here.

class Faculty(models.Model):
    name=models.CharField(max_length=20)
    faculty_dean=models.CharField(max_length=40,default='none')
    faculty_info=models.TextField(default="unknown")
    def __str__(self):
        return self.name

class Department(models.Model):
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    office_place=models.CharField(max_length=50,default='ds')

    def __str__(self):
        return self.name

class Employee(models.Model):
    department_employees=models.ForeignKey(Department,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    office_place=models.CharField(max_length=50,default=' ')
    

    def __str__(self):
        return self.first_name



class Image(models.Model):
    image = VersatileImageField(
        'Image',
        upload_to='images/',
        ppoi_field='image_ppoi'
    )
    image_ppoi = PPOIField()

