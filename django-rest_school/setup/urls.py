from django.contrib import admin
from django.urls import include, path
from school.views import CourseViewSet, ListRegistrationStudent, RegistrationViewSet, StudentViewSet, ListRegistrationCourse
from rest_framework import routers

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API documentation",
      default_version='v1',
      description="School API documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

router = routers.DefaultRouter()
router.register(r"students", StudentViewSet, basename="Student")
router.register(r"courses", CourseViewSet, basename="Course")
router.register(r"registrations", RegistrationViewSet, basename="Registration")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("students/<int:pk>/registrations/",ListRegistrationStudent.as_view(),),
    path("courses/<int:pk>/registrations/",ListRegistrationCourse.as_view(),),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
