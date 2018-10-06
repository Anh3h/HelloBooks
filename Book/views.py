from django.http import Http404
from rest_framework import status, generics
from rest_framework.response import Response

from Book.models import Book, Topic
from .serializers import BookSerializer, TopicSerializer


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, format=None):
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

    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_book(self, book_id):
        try:
            return Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        book = self.get_book(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        prev_book = self.get_book(pk)
        serializer = BookSerializer(prev_book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TopicList(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def get(self, request, format=None):
        topic = Topic.objects.all()
        serializer = TopicSerializer(topic, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = TopicSerializer(data=request.data,)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def get_topic(self, topic_id):
        try:
            return Topic.objects.get(pk=topic_id)
        except Topic.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        topic = self.get_topic(pk)
        serializer = TopicSerializer(topic)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        prev_topic = self.get_topic(pk)
        serializer = TopicSerializer(prev_topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
