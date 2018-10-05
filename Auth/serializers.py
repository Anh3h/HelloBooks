from rest_framework import serializers

from Auth.models import Profile
from Book.serializers import BookSerializer


class ProfileSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Profile
        fields = ('user', 'telephone', 'dob', 'address')


class FavBooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('favorite_books',)


class ReadingListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('reading_list',)
