from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView 
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated  
from account.permissions import IsAuthenticatedCustom
from .bookSerializer import BookSerializer,AuthorSerializer
from django.views import View
from django.http import HttpResponse
from .models import Book,Author

# Create your views here.

class ResultsSetPagination(PageNumberPagination):
    """
    Custom pagination class for paginating queryset results.

    This pagination class extends DRF's PageNumberPagination and adds
    support for customizing the page size via query parameters.

    Attributes
    ----------
    page_size_query_param : str
        The query parameter name that clients can use to specify the page size.

    Notes
    -----
    By default, this pagination class uses the `page` and `page_size` query parameters
    to control pagination. It supports setting a maximum page size to avoid excessively
    large responses.
    """
       
    page_size_query_param = 'page_size'
    

class Home(View):
    """
    A class-based view that handles GET requests to the home page.

    This view returns a simple HTTP response with the message 'API is Running!'.
    
    Methods
    -------
    get(request)
        Handles GET requests and returns an HTTP response with a status message.
    """
    def get(self,request):
        """
        Handles GET requests to the home page.

        Parameters
        ----------
        request : HttpRequest
            The HTTP request object.

        Returns
        -------
        HttpResponse
            An HTTP response with a message indicating that the API is running.
        """
        return HttpResponse('API is Running!')
    

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


