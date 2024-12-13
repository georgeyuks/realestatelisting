from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.CharField(max_length=50)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name
