from django.db.utils import IntegrityError
from django.test import TestCase
from django.utils import timezone


from projects.models import Project
from oauth.models import User
# Create your tests here.



class ProjectTests(TestCase):
    def test_create_project(self):
        owner = User.objects.create(username="owner", password="password") 
        project = Project.objects.create(owner=owner, title="Test Project")

        self.assertIn(project, Project.objects.filter(owner=owner))
    
    def test_different_owners(self):
        owner1 = User.objects.create(username="owner1", password="password") 
        owner2 = User.objects.create(username="owner2", password="password") 
        project1 = Project.objects.create(owner=owner1, title="Project1")
        project2 = Project.objects.create(owner=owner2, title="Project2")

        self.assertIn(project1, Project.objects.filter(owner=owner1))
        self.assertIn(project2, Project.objects.filter(owner=owner2))
        self.assertNotIn(project1, Project.objects.filter(owner=owner2))
        self.assertNotIn(project2, Project.objects.filter(owner=owner1))