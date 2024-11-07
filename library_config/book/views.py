from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import BookSerializers, AuthorSerializers
from .models import Book, Author

from rest_framework import generics


# Create your views here.

class BookListAPiViews(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class BookDetailApiViews(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookCreateApiViews(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class BookUpdateApiViews(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class BookDeleteApiViews(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class AuthorListApiViews(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers


@api_view(['GET'])
def book_list_views(request, *args, **kwargs):
    books = Book.objects.all()
    serializer = BookSerializers(books, many=True)

    return Response(serializer.data)
