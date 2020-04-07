import os

import requests
from django.db import models


# Create your models here.

def path_and_rename(path):
    def inner(instance, filename):
        ext = filename.split('.')[-1]
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            from uuid import uuid4
            filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(path, filename)
    return inner

class Author(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to=path_and_rename('authors'), null=True, blank=True)

    def _get_bar(self):
        return_value = requests.get('http://google.com', {'q': 'some search query'}).text
        return return_value

    bar = property(_get_bar)

    def __str__(self):
        return self.name


class Biography(models.Model):
    date_born = models.DateField("date_born")
    place_born = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    author = models.OneToOneField(to=Author, related_name='biography', on_delete=models.CASCADE)

    def __str__(self):
        return 'biography of {}'.format(self.author.name)


class Book(models.Model):
    title = models.CharField(max_length=255)
    year = models.DateField("date published")
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Reader(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, through='Lend')

    def __str__(self):
        return self.name


class Lend(models.Model):
    book = models.ForeignKey(Book, related_name="lends", on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, related_name="lends", on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return (str(self.book) + " -> " + str(self.reader))
