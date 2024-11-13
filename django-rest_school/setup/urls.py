from django.contrib import admin
from django.urls import include, path
from school.views import CourseViewSet, ListRegistrationStudent, RegistrationViewSet, StudentViewSet, ListRegistrationCourse
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"students", StudentViewSet, basename="Student")
router.register(r"courses", CourseViewSet, basename="Course")
router.register(r"registrations", RegistrationViewSet, basename="Registration")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("students/<int:pk>/registrations/",ListRegistrationStudent.as_view(),),
    path("courses/<int:pk>/registrations/",ListRegistrationCourse.as_view(),),
]
