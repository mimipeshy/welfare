from django.db import models


# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length = 30)