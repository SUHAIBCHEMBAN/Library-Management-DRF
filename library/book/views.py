from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView 
from .bookSerializer import BookSerializer,AuthorSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache
from .models import Book,Author
from .permissions import Owner

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
    pagination_class = ResultsSetPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        books = cache.get('books_cache')
        if not books:
            print("DATA Fetched from DB (book)")
            books = Book.objects.select_related('Author').all()
            cache.set('books_cache',books,timeout= 24 * 3600)
        else:
            print('DATA Fetched from CACHE (booklist)')
        return books
    
    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)


#TODO:ADD CACHE WITH SIGNELS NEW BOOK ADD TIME SIGNEL WORK AND CLEAN THE CACHE 

class BookRetriveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, and deleting a specific book.

    This view provides GET, PUT, PATCH, and DELETE methods for retrieving,
    updating, and deleting a specific book identified by its ID.
    """
     
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated,Owner]

    def get_queryset(self):
        books = cache.get('books_cache')
        if not books:
            print("DATA Fetched from DB (book)")
            books = Book.objects.select_related('Author').all()
            cache.set('books_cache',books,timeout= 24 * 3600)
        else:
            print('DATA Fetched from book CACHE (bookupdate)')
        return books


#TODO:ADD CACHE WITH SIGNELS NEW BOOK REMOVE TIME SIGNEL WORK AND CLEAN THE CACHE , SET THE PERMISSION


class AuthorListCreateAPIView(ListCreateAPIView):
    """
    API endpoint for listing and creating authors.

    This view provides GET and POST methods for listing and creating authors.
    The related books are prefetched to optimize query performance.
    """

    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        authors = cache.get('authors_cache')
        if not authors:
            print("DATA Fetched from DB (author)")
            authors = Author.objects.prefetch_related('book_set').all()
            cache.set('authors_cache',authors,timeout= 24 * 3600)
        else:
            print('DATA Fetched from Author CACHE (authorlist)')
        return authors

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)


#TODO:ADD CACHE WITH SIGNELS NEW AUTHOR ADD TIME SIGNEL WORK AND CLEAN THE CACHE 

class AuthorRetriveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, and deleting a specific author.

    This view provides GET, PUT, PATCH, and DELETE methods for retrieving,
    updating, and deleting a specific author identified by its ID.
    The related books are prefetched to optimize query performance.
    """
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated,Owner]

    def get_queryset(self):
        authors = cache.get('authors_cache')
        if not authors:
            print("DATA Fetched from DB (author)")
            authors = Author.objects.prefetch_related('book_set').all()
            cache.set('authors_cache',authors,timeout= 24 * 3600)
        else:
            print('DATA Fetched from CACHE (authorupdate)')
        return authors

    
#TODO:ADD CACHE WITH SIGNELS NEW AUTHOR REMOVE OR UPDATE TIME SIGNEL WORK AND CLEAN THE CACHE ,SET THE PERMISSION , LEARN ABOUT MODEL MANAGE USING DJANGO 


