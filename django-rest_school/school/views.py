from school.models import Course, Registration, Student
from school.serializers import CourseSerializer, ListRegistrationStudentSerializer, RegistrationSerializer, StudentSerializer, StudentSerializerV2
from rest_framework import generics, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

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
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


class ListRegistrationStudent(generics.ListAPIView):
    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs["pk"])
        return queryset

    serializer_class = ListRegistrationStudentSerializer
    
class ListRegistrationCourse(generics.ListAPIView):
    def get_queryset(self):
        queryset = Registration.objects.filter(course_id=self.kwargs["pk"])
        return queryset

    serializer_class = ListRegistrationStudentSerializer
