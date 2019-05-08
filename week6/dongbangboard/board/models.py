from django.db import models

# Create your models here.
class Message(models.Model):
    words = models.CharField(max_length=100)
    writter = models.CharField(max_length=20)
    date = models.DateField()