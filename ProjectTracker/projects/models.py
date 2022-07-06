from django.conf import settings
from django.db import models

# Create your models here.

class Project(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)

    
