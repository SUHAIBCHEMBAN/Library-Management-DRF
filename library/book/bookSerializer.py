from rest_framework import serializers
from .models import Book,Author

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.

    This serializer converts the Book model instances to JSON format and
    validates the data for creating and updating Book instances.

    """
    
    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ['added_by'] 


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.

    This serializer converts the Author model instances to JSON format and
    validates the data for creating and updating Author instances. It includes
    a nested representation of the books related to the author.

    """

    books = BookSerializer(many=True, read_only=True, source='book_set')
    
    class Meta:
        model = Author
        fields = '__all__'
        read_only_fields = ['added_by'] 
