from rest_framework import serializers
from school.models import Course, Registration, Student
from school.validators import cpf_invalid, cellphone_invalid, data_birth_invalid, name_invalid


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "name", "email", "cpf", "data_birth", "cellphone"]
        
        def validate(self, data):
            if cpf_invalid(data['cpf']):
                raise serializers.ValidationError({"cpf":"CPF must only contain numbers"})
            if len(data['cpf']) != 11:
                raise serializers.ValidationError({"cpf":"CPF must have 11 digits"})
            
            if name_invalid(data['name']):
                raise serializers.ValidationError({"name":"Name must only contain letters"})
            
            if data_birth_invalid(data['data_birth']):
                raise serializers.ValidationError({"data_birth":"Date of birth can't be greater than or equal to the current date"})
            
            if cellphone_invalid(data['cellphone']):
                raise serializers.ValidationError({"cellphone":"Cellphone must have 13 digits"})

            return data

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
