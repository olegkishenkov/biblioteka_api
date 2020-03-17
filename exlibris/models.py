from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255)

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
