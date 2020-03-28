from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from requests import Response
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

    def list(self, *args, **kwargs):
        return_value = super().list(self, *args, **kwargs)
        return return_value

    def retrieve(self, request, *args, **kwargs):
        return_value = super().retrieve(self, request, *args, **kwargs)
        author = Author.objects.get(pk=kwargs['pk'])
        return_value.data['bar'] = author.bar
        return return_value


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

def author_detail(request, id):
    try:
        author = Author.objects.get(id=id)
    except Author.DoesNotExist:
        return JsonResponse(status=404)
    if request.method == 'GET':
        serializer = AuthorSerializer(author)
        return JsonResponse(serializer.data)



def just_a_math_view(request):
    key = int(request.GET['key'])
    if key < 0:
        return_value = 1
    elif 0 <= key and key < 10:
        return_value = 2
    else:
        return_value = 3
    return HttpResponse(return_value)

