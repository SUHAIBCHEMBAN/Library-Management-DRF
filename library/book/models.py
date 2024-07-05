from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    """
    Model representing an author.
    """
    name = models.CharField(max_length=20)

    def __str__(self):
        """
        String representation of the Author object.
        """
        return self.name


class Book(models.Model):
    """
    Model representing a book.
    """
    Title = models.CharField(max_length=20)
    Author = models.ForeignKey(Author,on_delete=models.CASCADE)
    Published_date = models.DateField()

    def __str__(self):
        """
        String representation of the Book object.
        """
        return self.Title
