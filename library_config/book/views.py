from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import BookSerializers, AuthorSerializers
from .models import Book, Author



# class BookListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers

class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    lookup_field = 'pk'


class BookCreateAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    lookup_field = 'pk'


class BookRetrieveUpdateDestroyAPIView(APIView):

    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializers(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializers(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk)

        if book.author != request.user:
            return Response({"detail": "Siz faqat oz kitoblaringizni ochira olasiz."},
                            status=status.HTTP_403_FORBIDDEN)

        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AuthorRetrieveAPIView(APIView):

    def get(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        serializer = AuthorSerializers(author)
        return Response(serializer.data)
