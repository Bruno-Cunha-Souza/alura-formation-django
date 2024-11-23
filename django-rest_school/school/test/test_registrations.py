from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse

class RegistrationsTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Registration-list')
        self.client.force_authenticate(user=self.user)