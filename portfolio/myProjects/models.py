from django.db import models
from django.urls import reverse


# Create your models here.

# Мои проекты
class MyProject(models.Model):
    image = models.ImageField(upload_to='MyProjects/static/images', blank=True)
    urlProject = models.CharField(max_length=200)
    nameProject = models.CharField(max_length=200)
