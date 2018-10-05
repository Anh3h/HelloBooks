from django.contrib.auth.models import User
from django.db import models

from Book.models import Book


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, primary_key=True)
    telephone = models.CharField(max_length=13, blank=True, default='')
    dob = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=30, blank=True, default='')
    favorite_books = models.ManyToManyField(Book, related_name='user_fav_books')
    reading_list = models.ManyToManyField(Book, related_name='user_reading_list')
