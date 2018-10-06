from rest_framework import serializers

from Book.models import Book, Topic
from Transaction.models import Comment


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


class CommentReadOnlySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.user.username')

    class Meta:
        model = Comment
        fields = ('user', 'text')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user', 'book', 'text')


class BookCommentSerializer(serializers.ModelSerializer):
    comments = CommentReadOnlySerializer(read_only=True, many=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'isbn', 'author', 'edition', 'topic', 'publisher', 'publication_date', 'link',
                  'up_votes', 'down_votes', 'comments')
