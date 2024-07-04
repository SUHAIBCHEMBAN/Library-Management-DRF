from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Book(models.Model):
    Title = models.CharField(max_length=20)
    Author = models.ForeignKey(Author,on_delete=models.CASCADE)
    Published_date = models.DateField()

    def __str__(self):
        return self.Title
