from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Book, Publisher
from rest_framework.decorators import api_view
from class_project.models import Book
from rest_framework.response import responses, Response
from .serializer import BookSerializer, PublisherSerializer


# def index(request):
#     context = [1, 4, 5, 7]
#     text = "sgsnx dbdnskjs sjsnjd sunajsnsjn"
#     return render(request, 'my_app/index.html',
#                   context={'abc': context, 'name': "Amaka", 'is_major': True, 'text': text})
#
#
# def about(request):
#     return render(request, 'my_app/about.html')
#
#
# def redirect(request):
#     print(reverse('my_app:redirect_to_about'))
#     return HttpResponseRedirect(reverse('my_app:redirect_to_about'))
#
#
# def book_list(request):
#     # books = Book.objects.all()
#     # books = Book.objects.filter(genre='ROMANCE')
#     books = Book.objects.filter(publisher_id__in=(1, 7, 3)).order_by('title')
#
#     return render(request, 'my_app/book-list.html', {'books': list(books)})
#
#
# def book_detail(request, pk):
#     # try:
#     #     book = Book.objects.get(pk=pk)
#     #     return render(request, 'my_app/book-detail.html', {'book': book})
#     # except Book.DoesNotExist:
#     #     return HttpResponse("Good bye")
#     book = get_object_or_404(Book, pk=pk)
#     return render(request, 'my_app/book-detail.html', {'book': book})


@api_view()
def book_list(request):
    queryset = Book.objects.all()
    serializer = BookSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    serializer = BookSerializer(book)
    return Response(serializer.data)


@api_view()
def publisher_list(request):
    queryset = Publisher.objects.all()
    serializer = PublisherSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view
def publisher_detail(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    serializer = PublisherSerializer(publisher)
    return Response(serializer.data)
