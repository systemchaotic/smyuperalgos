```python
from django.test import TestCase
from django.urls import reverse
from .models import User, Content

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="testuser", password="testpassword")

    def test_user_creation(self):
        user = User.objects.get(username="testuser")
        self.assertEqual(user.username, 'testuser')

class ContentViewTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="testuser", password="testpassword")
        Content.objects.create(title="Test Content", body="This is a test content.", author=User.objects.get(username="testuser"))

    def test_content_view(self):
        response = self.client.get(reverse('content_detail', args=(1,)))
        self.assertEqual(response.status_code, 200)

class LoginViewTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="testuser", password="testpassword")

    def test_login_view(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)
```
