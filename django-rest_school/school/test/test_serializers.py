from django.test import TestCase
from school.models import Student
from school.serializers import StudentSerializer

class StudentSerializerTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            name = 'Nome De Estudante Teste',
            email = 'test@email.com',
            cpf= '68195899056',
            data_birth = '2000-01-01',
            cellphone = '86 99999-9999'
        )
        self.serializer_student = StudentSerializer(instance=self.student)
        
    def test_verify_fields_serialized(self):
        data = self.serializer_student.data
        self.assertEqual(set(data.keys()), set(['id', 'name', 'email', 'cpf', 'data_birth', 'cellphone']))
        
    def test_verify_content_fields_serialized(self):
        data = self.serializer_student.data
        self.assertEqual(data['id'], self.student.id)
        self.assertEqual(data['name'], self.student.name)
        self.assertEqual(data['email'], self.student.email)
        self.assertEqual(data['cpf'], self.student.cpf)
        self.assertEqual(data['data_birth'], self.student.data_birth)
        self.assertEqual(data['cellphone'], self.student.cellphone)