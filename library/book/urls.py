from django.urls import path
from . import views

urlpatterns = [

    # Show the Running Message
    path('',views.Home.as_view(),name='Home'),   

    # List and Create the books
    path('books/',views.BookListCreateAPIView.as_view(),name='books-create-list'),

    # Retrive,update and delete the books
    path('books/<int:pk>/',views.BookRetriveUpdateDeleteAPIView.as_view(),name='books-delete-update-retrive'),

    # List and Create the Author
    path('authors/',views.AuthorListCreateAPIView.as_view(),name='author-create-list'),

    # Retrive,Update and Delete the Author
    path('authors/<int:pk>/',views.AuthorRetriveUpdateDeleteAPIView.as_view(),name='author-delete-update-retrive'),

]


