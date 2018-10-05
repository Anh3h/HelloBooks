from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from Book.models import Book
from .serializers import BookSerializer


class BookList(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        if 'author' in request.query_params:
            if 'sort' in request.query_params:
                if request.query_params['sort'] is 0:
                    books = Book.objects.all().filter(author=request.query_params['author']).order_by('up_votes')
                else:
                    books = Book.objects.all().filter(author=request.query_params['author']).order_by('up_votes')\
                        .reverse()
            else:
                books = Book.objects.all().filter(author=request.query_params['author'])
        elif 'topic' in request.query_params:
            if 'sort' in request.query_params:
                if request.query_params['sort'] is 0:
                    books = Book.objects.all().filter(topic=request.query_params['topic']).order_by('up_votes')
                else:
                    books = Book.objects.all().filter(topic=request.query_params['topic']).order_by('up_votes')\
                        .reverse()
            else:
                books = Book.objects.all().filter(topic=request.query_params['topic'])
        else:
            if 'sort' in request.query_params:
                if request.query_params['sort'] is 0:
                    books = Book.objects.all().order_by('up_votes')
                else:
                    books = Book.objects.all().order_by('up_votes').reverse()
            else:
                books = Book.objects.all()

        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookDetails(APIView):

    def get_book(self, book_id):
        try:
            return Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        book = self.get_book(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)