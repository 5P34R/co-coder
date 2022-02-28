from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.user_data = {
            'username':'testuser',
            'email':'tester@mail.com',
            'password1': 'Password@123',
            'password2': 'Password@123',
        }

        self.index_url = reverse('core:index')
        self.signup_url = reverse('core:signup')
        self.login_url = reverse('core:login')

    def test_index_page(self):
        response = self.client.get(self.index_url)
        if self.assertEquals(response.status_code, 302):
            self.test_registration_check_GET()

    def test_login_redirect_check_GET(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed('auth/login.html')
    
    def test_registration_check_GET(self):
        response = self.client.get(self.signup_url)
        self.assertTemplateUsed('auth/signup.html')
        if self.assertEquals(response.status_code, 200):
            self.test_registration_check_POST()

    def test_registration_check_POST(self):
        response = self.client.post(self.signup_url, self.user_data, content_type='text/html')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('auth/signup.html')