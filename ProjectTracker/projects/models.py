from django.utils import timezone 
from django.conf import settings
from django.core.validators import ValidationError, MaxLengthValidator
from django.forms import ModelForm
from django.db import models
from oauth.models import User
# Create your models here.

class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=60, validators=[MaxLengthValidator(60)])
    slug = models.SlugField(max_length=120, validators=[MaxLengthValidator(120)])
    total_time = models.PositiveIntegerField(default=0)
    last_worked_on = models.DateTimeField(default=timezone.now)

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title',]

class Session(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    total_time = models.PositiveIntegerField(default=0)

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError('Start date is after end date')
        
class SessionForm(ModelForm):
    class Meta:
        model = Session
        fields = ['start_date', 'end_date', 'total_time',]

class Milestone(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateTimeField()
    description = models.CharField(max_length=200, validators=[MaxLengthValidator(200)])

    
     

    
