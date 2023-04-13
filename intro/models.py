from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='photos/')
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    education = models.TextField()
    work_experience = models.TextField()
    project_experience = models.TextField()
    social_links = models.TextField()
    skills = models.TextField()
    languages = models.TextField()
    hobbies = models.TextField()
