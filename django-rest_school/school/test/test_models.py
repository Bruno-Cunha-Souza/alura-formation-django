from django.test import TestCase
from school.models import Student

class modelStudentTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            name = 'Nome De Estudante Teste',
            email = 'test@email.com',
            cpf= '68195899056',
            data_birth = '2000-01-01',
            cellphone = '86 99999-9999'
        )
        
    def test_checks_student_attribute(self):
        self.assertEqual(self.student.name, 'Nome De Estudante Teste')
        self.assertEqual(self.student.email, 'test@email.com')
        self.assertEqual(self.student.cpf, '68195899056')
        self.assertEqual(self.student.data_birth, '2000-01-01')
        self.assertEqual(self.student.cellphone, '86 99999-9999')