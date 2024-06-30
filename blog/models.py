from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.db.models.base import Model
from django.db.models.signals import pre_save
from boma.utils import unique_slug_generator

class
class
class
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default='Blog Post')
    slug = models.SlugField(max_length=255, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='blog', null=True)
    