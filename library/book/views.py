from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView 
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated  
from .bookSerializer import BookSerializer,AuthorSerializer
from .models import Book,Author

# Create your views here.

class ResultsSetPagination(PageNumberPagination):
    """
    Custom pagination class for paginating queryset results.

    This pagination class extends DRF's PageNumberPagination and adds
    support for customizing the page size via query parameters.
    """
       
    page_size_query_param = 'page_size'
    

class BookListCreateAPIView(ListCreateAPIView):

    """
    API endpoint for listing and creating books.

    This view provides GET and POST methods for listing and creating books.
    """

    serializer_class = BookSerializer
    queryset = Book.objects.select_related('Author').all()
    pagination_class = ResultsSetPagination
    permission_classes = [IsAuthenticated]


class BookRetriveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, and deleting a specific book.

    This view provides GET, PUT, PATCH, and DELETE methods for retrieving,
    updating, and deleting a specific book identified by its ID.
    """
     
    serializer_class = BookSerializer
    queryset = Book.objects.select_related('Author').all()
    permission_classes = [IsAuthenticated]


class AuthorListCreateAPIView(ListCreateAPIView):
    """
    API endpoint for listing and creating authors.

    This view provides GET and POST methods for listing and creating authors.
    The related books are prefetched to optimize query performance.
    """

    serializer_class = AuthorSerializer
    queryset = Author.objects.prefetch_related('book_set').all()
    permission_classes = [IsAuthenticated]


class AuthorRetriveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, and deleting a specific author.

    This view provides GET, PUT, PATCH, and DELETE methods for retrieving,
    updating, and deleting a specific author identified by its ID.
    The related books are prefetched to optimize query performance.
    """
    
    serializer_class = AuthorSerializer
    queryset = Author.objects.prefetch_related('book_set').all()
    permission_classes = [IsAuthenticated]


