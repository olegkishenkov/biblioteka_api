from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework import permissions
from .models import Author, Biography, Book, Reader, Lend
from .serializers import AuthorSerializer, BiographySerializer, BookSerializer, ReaderSerializer, LendSerializer
import requests

# Create your views here.
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]

class BiographyViewSet(viewsets.ModelViewSet):
    queryset = Biography.objects.all().order_by('author__name')
    serializer_class = BiographySerializer
    permission_classes = [permissions.AllowAny]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class ReaderViewSet(viewsets.ModelViewSet):
    queryset = Reader.objects.all().order_by('name')
    serializer_class = ReaderSerializer
    permission_classes = [permissions.AllowAny]

class LendViewSet(viewsets.ModelViewSet):
    queryset = Lend.objects.all().order_by('date_start')
    serializer_class = LendSerializer
    permission_classes = [permissions.AllowAny]

def author_list(request):
    if request.method == "GET":
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return JsonResponse(serializer.data, safe=False)

