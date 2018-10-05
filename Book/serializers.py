from rest_framework import serializers

from Book.models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'isbn', 'author', 'edition', 'publisher', 'publication_date', 'link',
                  'up_votes', 'down_votes')
