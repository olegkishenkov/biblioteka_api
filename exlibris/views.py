from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework import permissions
from .models import Author, Biography
from .serializers import AuthorSerializer, BiographySerializer


# Create your views here.
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]


class BiographyViewSet(viewsets.ModelViewSet):
    queryset = Biography.objects.all().order_by('author__name')
    serializer_class = BiographySerializer
    permission_classes = [permissions.AllowAny]
