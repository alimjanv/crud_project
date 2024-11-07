from django.urls import path

from .views import BookListAPiViews, BookDetailApiViews, AuthorListApiViews, book_list_views, BookDeleteApiViews, \
    BookUpdateApiViews, BookCreateApiViews

urlpatterns = [
    path('books', BookListAPiViews.as_view()),
    path('books/create/', BookCreateApiViews.as_view()),
    path('<int:pk>/detail', BookDetailApiViews.as_view()),
    path('<int:pk>/delete', BookDeleteApiViews.as_view()),
    path('<int:pk>/update', BookUpdateApiViews.as_view()),
    path('authors', AuthorListApiViews.as_view()),
    path('f_books', book_list_views)
]
