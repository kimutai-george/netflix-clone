from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.
AGE_CHOICES = (
    ('All','All'),
    ('Kids','Kids')
)

MOVIE_CHOICES = (
    ('Seasonal','Seasonal'),
    ('Single','Single')
)

class Profile(models.Model):
    name = models.CharField(max_length=255)
    age_limit = models.CharField(max_length=10,choices=AGE_CHOICES)
    uuid = models.UUIDField(default=uuid.uuid4)

class CustomUser(AbstractUser):
    profile = models.ManyToManyField(Profile,blank=True)

class Videos(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    file = models.FileField(upload_to='movies')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    type = models.CharField(max_length=30,choices=MOVIE_CHOICES)
    videos = models.ManyToManyField(Videos)
    flyer = models.ImageField(upload_to='flyers')
    age_limit = models.CharField(max_length=10,choices=AGE_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4)





