from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Project, Task
from datetime import date

class AuthTestCase(APITestCase):
    def setUp(self):
        self.username = 'testuser111'
        self.password = 'testpass123451'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.token_url = reverse('token_obtain_pair')

    def test_obtain_token_success(self):
        response = self.client.post(self.token_url, {
            'username': self.username,
            'password': self.password
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_obtain_token_invalid_credentials(self):
        response = self.client.post(self.token_url, {
            'username': self.username,
            'password': 'wrongpassword'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('detail', response.data)

    def test_delete_project(self):
        self.client.force_authenticate(user=self.user)
        project = Project.objects.create(name='My Project', description='...', owner=self.user, start_date=date.today(), end_date=date.today())
        response = self.client.delete(f'/api/projects/{project.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Project.objects.filter(id=project.id).exists())
    
    def test_delete_task(self):
        self.client.force_authenticate(user=self.user)
        project = Project.objects.create(
            name='My Project',
            description='...',
            owner=self.user,
            start_date=date.today(),
            end_date=date.today()
        )
        task = Task.objects.create(
            title='To be deleted',
            project=project,
            description='Some task description',
            status='todo',
            due_date=date.today()
        )
        response = self.client.delete(f'/api/tasks/{task.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=task.id).exists())