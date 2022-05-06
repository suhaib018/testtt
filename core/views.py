from tkinter import image_names
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .aiModel import *
import re
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import Image
from .serializers import ImageSerializer
from rest_flex_fields.views import FlexFieldsModelViewSet
import matplotlib.pyplot as plt


# Create your views here.


def index(request):
    #read image from computer
    path=plt.imread("C:\\Users\\derar\\Desktop\\project_graduation_images\\ku.jpg")
    faculty_name=return_faculty_name(path)

    updated_faculty_name=re.sub('[123]',"",faculty_name)

    updated_faculty_name=updated_faculty_name.lower()

    faculties_ids={
        "kasit":1,
        "medicine":2,
        "engineering":3,
        "shareeah":4,
        "business":5,
        "law":7,
        "kitchen":8,
    }

    #get faculty id
    for key in faculties_ids:
        if key==updated_faculty_name:
            faculty_id=faculties_ids[key]
            break
    
    # print(faculty_id)

    facility = Faculty.objects.get(id=1)
    employees=Employee.objects.filter(department_employees__faculty_id=facility.id)[:5]
    return render(request,'index.html',{'emps':employees})
    
class FacultyViewSet(viewsets.ModelViewSet):

    # API endpoint that allows users to be viewed or edited.
        queryset = Faculty.objects.all()
        serializer_class = FacultySerializer
        permission_classes = [permissions.IsAuthenticated]

class DepartmentViewSet(viewsets.ModelViewSet):

    # API endpoint that allows users to be viewed or edited.
        queryset = Department.objects.all()
        serializer_class = DepartmentSerializer
        permission_classes = [permissions.IsAuthenticated]

class employeeViewSet(viewsets.ModelViewSet):

    # API endpoint that allows users to be viewed or edited.
        queryset = Employee.objects.all()
        serializer_class = EmployeeSerializer
        permission_classes = [permissions.IsAuthenticated]
        
class ImageViewSet(FlexFieldsModelViewSet):

    serializer_class = ImageSerializer
    queryset = Image.objects.all()