from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework import serializers

from Auth.models import Profile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
        extra_kwargs = {
            'username': {
                'validators': [UnicodeUsernameValidator()]
            }
        }


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ('user', 'telephone', 'dob', 'address')

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer
        :param validated_data: data containing ALL the details of a User
        :return: return a successfully created user account
        """

        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        profile = Profile.objects.create(user=user, **validated_data)
        return profile

    def update(self, instance, validated_data):
        """
        Overriding the default update method of the Model serializer
        :param validated_data: data containing ALL the details of a User
        :return: return a successfully created user account
        """

        user_data = validated_data.pop('user')
        user = UserSerializer.update(UserSerializer(), User.objects.get(username=instance.user),
                                     validated_data=user_data)
        instance.telephone = validated_data.pop('telephone')
        instance.address = validated_data.pop('address')
        instance.dob = validated_data.pop('dob')
        instance.save()
        return instance


class FavBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('favorite_books',)


class ReadingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('reading_list',)
