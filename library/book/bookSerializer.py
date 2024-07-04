from rest_framework import serializers
from .models import Book,Author

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.

    This serializer converts the Book model instances to JSON format and
    validates the data for creating and updating Book instances.

    Meta Attributes:
        model (Book): The model that is being serialized.
        fields (str): A string that specifies that all fields in the model should be included in the serialized data.
    """
    
    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.

    This serializer converts the Author model instances to JSON format and
    validates the data for creating and updating Author instances. It includes
    a nested representation of the books related to the author.

    Attributes:
        books (BookSerializer): A nested serializer to represent the books
        written by the author. This field is read-only and uses the default
        reverse relation name 'book_set' provided by Django for the ForeignKey
        relationship from Book to Author.

    Meta Attributes:
        model (Author): The model that is being serialized.
        fields (str): A string that specifies that all fields in the model
        should be included in the serialized data.
    """

    books = BookSerializer(many=True, read_only=True, source='book_set')
    
    class Meta:
        model = Author
        fields = '__all__'
