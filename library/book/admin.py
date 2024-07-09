from django.contrib import admin
from .models import Author,Book

# Register your models here.

class AdminAuthor(admin.ModelAdmin):
    """
    Admin interface options for the Author model.

    This class customizes the display and filter options for the Author model
    in the Django admin interface.
    """
    list_display = ['id','name','added_by']
    list_filter = ['id','added_by']

class AdminBook(admin.ModelAdmin):
    """
    Admin interface options for the Book model.

    This class customizes the display and filter options for the Book model
    in the Django admin interface.
    """
    list_display = ['id','Title','Author','Published_date','added_by']
    list_filter = ['id','Published_date','added_by']


# Register the models with the admin site using the custom admin classes
admin.site.register(Author,AdminAuthor)
admin.site.register(Book,AdminBook)

