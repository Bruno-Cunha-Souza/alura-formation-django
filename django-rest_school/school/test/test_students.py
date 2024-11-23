from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from school.models import Student
from school.serializers import StudentSerializer

class StudentsTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Student-list')
        self.client.force_authenticate(user=self.user)
        self.student_1 = Student.objects.create(name='Student 1', email='teste1@emmail.com', cpf='68224431002', data_birth='2024-01-01', cellphone='86 99999-9999')
        self.student_2 = Student.objects.create(name='Student 2', email='teste2@emmail.com', cpf='70261486055', data_birth='2024-01-02', cellphone='86 99999-9999')
    
    def test_get_students(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)    
    
    def test_get_students(self):
        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code, 200)
        
        student_data = Student.objects.get(pk=1)
        student_data_serialized = StudentSerializer(student_data).data
        self.assertEqual(response.data, student_data_serialized)
        
    def test_post_students(self):
        data = {
            'name': 'Student 3',
            'email': 'emailtestepost@email.com',
            'cpf': '82271917034',
            'data_birth': '2024-01-03',
            'cellphone': '86 99999-9999'   
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 201)
    
    def test_delete_students(self):
        response = self.client.delete(self.url+'2/')
        self.assertEqual(response.status_code, 204)
    
    #def test_put_students(self):
        