from school.models import Course, Registration, Student
from school.serializers import CourseSerializer, ListRegistrationStudentSerializer, RegistrationSerializer, StudentSerializer, StudentSerializerV2
from rest_framework import generics, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name', 'email', 'cpf']
    
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return StudentSerializerV2
        return StudentSerializer
        
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('id')
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class RegistrationAnonRateThrottle(AnonRateThrottle):
    rate = '3/day'

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all().order_by('id')
    serializer_class = RegistrationSerializer
    throttle_classes = [UserRateThrottle, RegistrationAnonRateThrottle]
    http_method_names = ['get', 'post', 'head']

class ListRegistrationStudent(generics.ListAPIView):
    """
    View Description:
    - Enrollment List by Student ID
    Parameters:
    - pk (int): The primary identifier of the object. It must be an integer.
    """
    
    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs["pk"])
        return queryset

    serializer_class = ListRegistrationStudentSerializer
    
class ListRegistrationCourse(generics.ListAPIView):
    """
    View Description:
    - Enrollment List by Registration ID
    Parameters:
    - pk (int): The primary identifier of the object. It must be an integer.
    """
    
    def get_queryset(self):
        queryset = Registration.objects.filter(course_id=self.kwargs["pk"])
        return queryset

    serializer_class = ListRegistrationStudentSerializer
