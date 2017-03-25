from django.db import models


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    salt = models.CharField(max_length=40, default='Null')
