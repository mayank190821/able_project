from ast import Str
from django.db import models
from django.forms import CharField, EmailField, EmailInput

class Companie(models.Model):
    name=models.CharField(max_length=20)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(primary_key=True)
    salt =models.CharField(max_length=100)
    def __str__(self):
        return self.username