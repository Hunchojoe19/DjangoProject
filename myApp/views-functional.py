from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.urls import reverse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import BookSerializer, PublisherSerializer

from .models import Book
from .models import Publisher
from django.db import connection
from django.db import transaction


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


#
# def book_list(request):
#     # books = Book.objects.all()
#     # books = Book.objects.filter(genre='FICTION')
#     # books = Book.objects.filter(title__icontains='MR')
#     # cursor = connection.cursor()
#     # result = cursor.execute("select * from myapp_book")
#     # books = Book.objects.all()
#     with transaction.atomic():
#         p1 = Publisher.objects.create(name="hhh", )
#         b1 = Book.objects.create(title="")
#     books = Book.objects.raw("select * from myapp_book")
#     # books = result.fetchall()
#     # cursor.close()
#     return render(request, 'myApp/book-list.html', {'books': list(books)})
#
#
# def book_details(request, pk):
#     # try:
#         # book = Book.objects.get(pk=pk)
#         # return render(request, 'myApp/book-detail.html', {'book': book})
#     # except Book.DoesNotExist:
#     #     return HttpResponse("Not found")
#     book = get_object_or_404(Book, pk=pk)
#     return render(request, 'myApp/book-detail.html', {'book': book})
@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def book_details(request, pk):
    # try:
    #     book = Book.objects.get(pk=pk)
    #     serializer = BookSerializer(book)
    #
    #     return Response(serializer.data)
    # except Book.DoesNotExist:
    #     return Response({"error": "could not find resource"}, status=status.HTTP_404_NOT_FOUND)
    book = get_object_or_404(Book, pk=pk, context={'request': request})
    if request.method == 'GET':
        serializer = BookSerializer(book, context={'request': request})

        return Response(serializer.data)
    elif request.method in ('PUT', 'PATCH'):
        serializer = BookSerializer(Book, data=request.data, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def publisher_list(request):
    if request.method == 'GET':
        queryset = Publisher.objects.all()
        serializer = PublisherSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PublisherSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def publisher_details(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk, context={'request': request})
    if request.method == 'GET':
        serializer = PublisherSerializer(publisher, context={'request': request})

        return Response(serializer.data)
    elif request.method in ('PUT', 'PATCH'):
        serializer = PublisherSerializer(Publisher, data=request.data, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        publisher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
