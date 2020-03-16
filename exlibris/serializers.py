from rest_framework import serializers
from .models import Author, Biography, Book, Reader, Lend


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['name']

class BiographySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Biography
        fields = ['date_born', 'place_born', 'education', 'author']

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'year', 'author']

class ReaderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reader
        fields = ['name', 'books']

class LendSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lend
        fields = ['book', 'reader', 'date_start', 'date_end', ]
