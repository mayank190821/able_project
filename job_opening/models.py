from django.db import models
from django.forms import CharField, EmailField, EmailInput

class NewJob(models.Model):
    email = models.EmailField(max_length=100,primary_key=True)
    jobRole=models.CharField(max_length=100)
    jobDesc = models.CharField(max_length=1000)
    place = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    def __str__(self):
        return self.email;
