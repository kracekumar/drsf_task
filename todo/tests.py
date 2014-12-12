import base64
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
# Create your tests here.


class TodoApiTestCase(APITestCase):
    def setUp(self):
        self.username = 'kracekumar'
        self.password = 'k'

        self.user = User.objects.create_user(username=self.username,
                                             password=self.password,
                                             email='foo@bar.com')
        # Django Rest Framework will use this for authentication for every request
        credentials = base64.b64encode('{}:{}'.format(
            self.username, self.password))
        self.client.defaults['HTTP_AUTHORIZATION'] = 'Basic ' + credentials

    def test_create_todo(self):
        url = reverse('todo-list')
        data = {'name': 'new idea', 'created_by': self.user.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
