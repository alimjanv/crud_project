from django.urls import path
from .views import BooksAPIView, BookRetrieveUpdateDestroyAPIView, AuthorRetrieveAPIView

urlpatterns = [
    #path('book-create/', BookCreateAPIView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail'),
    path('authors/<int:pk>/', AuthorRetrieveAPIView.as_view(), name='author-detail'),
    path('books/', BooksAPIView.as_view(), name='book-list'),



]
