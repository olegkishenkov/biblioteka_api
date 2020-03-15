from rest_framework import serializers
from .models import Author, Biography, Book, Reader, Lend


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']
