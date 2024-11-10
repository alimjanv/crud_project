from django.urls import path
from .views import BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView, AuthorRetrieveAPIView

urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail'),
    path('authors/<int:pk>/', AuthorRetrieveAPIView.as_view(), name='author-detail'),
]
