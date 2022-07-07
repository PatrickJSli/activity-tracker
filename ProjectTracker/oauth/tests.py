from django.db.utils import IntegrityError
from django.test import TestCase
from oauth.models import User 

# Create your tests here.


class UserTests(TestCase):
    def test_create_user(self):
        user = User.objects.create(username="test", password="password")
        self.assertEqual(User.objects.all()[0], user)
    
    def test_duplicate_username(self):
        user1 = User.objects.create(username="duplicate", email="test@test.com", password="password")
        with self.assertRaises(IntegrityError):
            User.objects.create(username="duplicate", email="test2@test.com", password="password")