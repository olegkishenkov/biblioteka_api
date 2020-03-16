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
