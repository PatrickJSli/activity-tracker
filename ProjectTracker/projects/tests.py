from django.db.utils import IntegrityError
from django.core.validators import ValidationError
from django.test import TestCase
from django.utils import timezone
import datetime


from projects.models import Project, Session
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

    def test_too_long_title(self):
        owner = User.objects.create(username="long_title_owner", password="password")
        title = "skdfjhbrenwsmkdfjhbednwmskdfgjhfbrdenmsdkfjhbrdeskdjfhbdnemkskdfjhnemwskdfjhr"
        project = Project.objects.create(owner=owner, title=title)
        with self.assertRaises(ValidationError):
            project.full_clean()

class SessionTests(TestCase):
    def setUp(self):
        self.owner1 = User.objects.create(username="session_owner1", password="password")
        self.owner2 = User.objects.create(username="session_owner2", password="password")
        self.project1 = Project.objects.create(owner=self.owner1, title="Project1") 
        self.project2 = Project.objects.create(owner=self.owner2, title="Project2")
        self.now = datetime.datetime.now()

    def test_create_session(self):
        session = Session.objects.create(project=self.project1, start_date=self.now, end_date=self.now + datetime.timedelta(days = 1))
        self.assertIn(session, Session.objects.all())
    
    def test_proper_project(self):
        session1 = Session.objects.create(project=self.project1, start_date=self.now, end_date=self.now + datetime.timedelta(days = 1))

        self.assertIn(session1, Session.objects.filter(project=self.project1))
        self.assertNotIn(session1, Session.objects.filter(project=self.project2))
    
    def test_start_after_end(self):
        session1 = Session.objects.create(project=self.project1, start_date=self.now, end_date=self.now - datetime.timedelta(days = 1))
        with self.assertRaises(ValidationError):
            session1.full_clean()

        