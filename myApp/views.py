from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rest_framework import status, request
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from myApp.models import Book, Publisher
from myApp.serializer import BookSerializer, PublisherSerializer


def index(request):
    context = 'Joseph'
    text = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab error fuga ipsa mollitia nesciunt non " \
           "provident qui quidem unde. Accusantium alias autem est expedita iusto nihil optio praesentium quaerat " \
           "totam! "
    return render(request, 'myApp/index.html', context={'name': context, 'is_major': True, 'text': text})


def about(request):
    return render(request, 'myApp/about.html')


def redirect(request):
    return HttpResponseRedirect(reverse('myApp:index'))
    # reverse would take the name of the app "myApp" and the path name "index", and provide the absolute path i.e
    # Localhost:8080...

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class PublisherList(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
