from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=30)
    isbn = models.CharField(blank='', max_length=20)
    author = models.CharField(max_length=30, blank='', null=True)
    edition = models.CharField(max_length=15, blank='', null=True)
    publisher = models.CharField(max_length=30, blank='', null=True)
    publication_date = models.DateField(null=True, blank='')
    link = models.CharField(max_length=100, blank='', null=True)
    up_votes = models.IntegerField()
    down_votes = models.IntegerField()
    downloads = models.IntegerField
    topic = models.ForeignKey(Topic, related_name='books', on_delete=models.CASCADE)
