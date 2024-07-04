from django.contrib import admin
from .models import Author,Book

# Register your models here.

class AdminAuthor(admin.ModelAdmin):
    """
    Admin interface options for the Author model.

    This class customizes the display and filter options for the Author model
    in the Django admin interface.

    Attributes:
        list_display (list): Specifies the fields to display in the list view.
        list_filter (list): Specifies the fields to filter by in the list view.
    """
    list_display = ['id','name']
    list_filter = ['id']

class AdminBook(admin.ModelAdmin):
    """
    Admin interface options for the Book model.

    This class customizes the display and filter options for the Book model
    in the Django admin interface.

    Attributes:
        list_display (list): Specifies the fields to display in the list view.
        list_filter (list): Specifies the fields to filter by in the list view.
    """
    list_display = ['id','Title','Author','Published_date']
    list_filter = ['id','Published_date']


# Register the models with the admin site using the custom admin classes
admin.site.register(Author,AdminAuthor)
admin.site.register(Book,AdminBook)

