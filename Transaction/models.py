from django.db import models

from Auth.models import Profile
from Book.models import Book


class Transaction(models.Model):

    STATUS = [('PND', 'PENDING'), ('ACT', 'ACCEPTED'), ('DND', 'DENIED'), ('CND', 'CANCELLED')]

    user = models.ForeignKey(Profile, related_name='transactions', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='transactions', on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(choices=STATUS, default='PND', max_length=10)
    created = models.DateField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(Profile, related_name='comments', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
