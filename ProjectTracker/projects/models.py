from wsgiref.validate import validator
from django.conf import settings
from django.core.validators import ValidationError, MaxLengthValidator
from django.db import models
from oauth.models import User
# Create your models here.

class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=60, validators=[MaxLengthValidator(60)])

class Session(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError('Start date is after end date')

    
     

    
