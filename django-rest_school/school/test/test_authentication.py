from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse

class AuthenticationUserTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Student-list')
        
    def test_authentication_user(self):
        user = authenticate(username='admin', password='admin')
        self.assertTrue((user is not None) and user.is_authenticated)
    
    def test_authentication_user_invalid(self):
        user = authenticate(username='admin', password='admin1')
        self.assertFalse((user is not None) and user.is_authenticated)
        
    def test_request_without_authentication(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)