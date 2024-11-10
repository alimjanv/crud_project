from django.urls import path
from .views import (
    BookListAPiViews, BookDetailApiViews, BookCreateApiViews, BookUpdateApiViews, BookDeleteApiViews, AuthorListApiViews, book_list_views)

urlpatterns = [
    path('books/', BookListAPiViews.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailApiViews.as_view(), name='book-detail'),
    path('books/create/', BookCreateApiViews.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateApiViews.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteApiViews.as_view(), name='book-delete'),
    path('authors/', AuthorListApiViews.as_view(), name='author-list'),
    path('books/list/', book_list_views, name='book-list-views')
]
