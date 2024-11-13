from django.contrib import admin
from django.urls import path, include
from school.views import StudentViewSet, CourseViewSet, RegistrationViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet, basename='Student')
router.register(r'courses', CourseViewSet, basename='Course')
router.register(r'registrations', RegistrationViewSet, basename='Registration')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
