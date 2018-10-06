from rest_framework import serializers

from Book.models import Book, Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('name',)


class BookSerializer(serializers.ModelSerializer):
    # topic = serializers.ReadOnlyField(source='topic.name')

    class Meta:
        model = Book
        fields = ('id', 'title', 'isbn', 'author', 'edition', 'topic', 'publisher', 'publication_date', 'link',
                  'up_votes', 'down_votes')
