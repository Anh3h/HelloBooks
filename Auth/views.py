from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from Auth.models import Profile
from .serializers import ProfileSerializer, FavBooksSerializer, ReadingListSerializer


class ProfileList(generics.ListCreateAPIView):
    """List all user profiles or create a new user profile"""

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get(self, request, format=None):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update and delete a profile instance"""

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_profile(self, profile_id):
        try:
            return Profile.objects.get(pk=profile_id)
        except Profile.DoesNotExist:
            raise Http404

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        prev_profile = self.get_profile(pk)
        serializer = ProfileSerializer(prev_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FavBooks(APIView):
    """Retrieve, add and delete a user's favorite books"""

    def get_profile(self, profile_id):
        try:
            return Profile.objects.get(pk=profile_id)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializer = FavBooksSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReadingList(APIView):
    """Retrieve, add and delete books to a user's reading list"""

    def get_profile(self, profile_id):
        try:
            return Profile.objects.get(pk=profile_id)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializer = ReadingListSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)


def api_root(request):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'books': reverse('book-list', request=request, format=format),
        'topics': reverse('topic-list', request=request, format=format),
    })
