from rest_framework import serializers
from school.models import Course, Registration, Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "name", "email", "cpf", "data_birth", "cellphone"]


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = "__all__"


class ListRegistrationStudentSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source="course.description")
    period = serializers.SerializerMethodField()

    class Meta:
        model = Registration
        fields = ["course", "period"]

    def get_period(self, obj):
        return obj.get_period_display()


class StudentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source="studante.name")

    class Meta:
        model = Student
        fields = ["student_name"]
