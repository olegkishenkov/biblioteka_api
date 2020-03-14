from rest_framework import serializers
from .models import Author, Biography, Book, Reader, Lend

class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return(Author.objects.create(**validated_data))

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        return instance

