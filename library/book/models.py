from datetime import date
from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    """
    Model representing an author.
    """
    name = models.CharField(max_length=20,default='Unknown Author')
    added_by = models.ForeignKey(User,on_delete=models.CASCADE, default=1)

    def __str__(self):
        """
        String representation of the Author object.
        """
        return self.name


class Book(models.Model):
    """
    Model representing a book.
    """
    Title = models.CharField(max_length=20,default="Untitled Book")
    Author = models.ForeignKey(Author,on_delete=models.CASCADE)
    Published_date = models.DateField(default=date.today)
    added_by = models.ForeignKey(User,on_delete=models.CASCADE, default=1)

    def __str__(self):
        """
        String representation of the Book object.
        """
        return self.Title
