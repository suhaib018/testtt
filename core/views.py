from tkinter import image_names
from django.shortcuts import render
from matplotlib.style import context
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
from rest_framework.views import APIView
from rest_framework.response import Response
from requests_toolbelt.multipart import MultipartDecoder
from .forms import *
import PIL.Image




# Create your views here.
def index(request):
    #read image from computer
    path=plt.imread("C:\\Users\\derar\\Desktop\\project_graduation_images\\k.jpg")
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
        'none':10,
    }

    #get faculty id
    for key in faculties_ids:
        if key==updated_faculty_name:
            faculty_id=faculties_ids[key]
            break

    if faculty_id == 10:
        return render(request,'TEMP.html')
    
    facility = Faculty.objects.get(id=faculty_id)
    employees=Employee.objects.filter(department_employees__faculty_id=facility.id)[:5]
    
    return render(request,'index.html',{'emps':employees,'data':facility})

#returns the right data referring to the right faculty

#EmployeeAndDepartmentList

class EmployeeAndDepartmentList(APIView):
    def post(self, request):
        #all employees
        # multipart_file = request.POST.get('image')
        database = Employee.objects.all()
        #parsed = MultiPartParser.parse(multiPartFile)
        img = PIL.Image.open(request.data.get('image'))
        return_faculty_name(img)
        
        #converts to JSON
        serializer_context = {

            'request': request,
        }
        serializer = EmployeeSerializer(database, many=True,context=serializer_context)
        #the received data

        receivedData = request.data

        #Returns data back to client

        # data=request.data
        # print(data['data'])
        return Response(serializer.data)


# def faculty_image_view(request):
  
#     if request.method == 'POST':
#         form = Faculty_Image(request.POST, request.FILES)
  
#         if form.is_valid():
#             form.save()
#             return redirect('success')
#     else:
#         form = Faculty_Image()
#     return render(request, 'index.html', {'form' : form})
  
  
# def success(request):
#     return HttpResponse('successfully uploaded')
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