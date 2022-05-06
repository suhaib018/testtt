from django.urls import path,include
from rest_framework import routers
from . import views
from django.contrib import admin
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()

router.register(r'faculties', views.FacultyViewSet)
router.register(r'departments', views.DepartmentViewSet)
router.register(r'employeies', views.employeeViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index, name='index'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



