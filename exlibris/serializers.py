from rest_framework import serializers
from .models import Author, Biography, Book, Reader, Lend


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['name']

class BiographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Biography
        fields = ['date_born', 'place_born', 'education', 'author']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        author = Author.objects.get(id=ret['author'])
        serializer = AuthorSerializer(author)
        ret['author'] = serializer.data
        return ret

    def to_internal_value(self, data):
        ret = super().to_internal_value(data)
        return ret

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


