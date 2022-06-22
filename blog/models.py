from django.db import models

# Create your models here.


class Post(models.Model):
    """A blog post"""
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField()
    published_date = models.DateTimeField()