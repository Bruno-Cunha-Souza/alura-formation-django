from school.models import Course, Registration, Student
from school.serializers import CourseSerializer, ListRegistrationStudentSerializer, RegistrationSerializer, StudentSerializer
from rest_framework import generics, viewsets


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


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
