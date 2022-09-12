from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from class_project.models import Book


def index(request):
    context = [1, 4, 5, 7]
    text = "sgsnx dbdnskjs sjsnjd sunajsnsjn"
    return render(request, 'my_app/index.html', context={'abc': context, 'name': "Amaka", 'is_major': True, 'text':text})


def about(request):
    return render(request, 'my_app/about.html')


def redirect(request):
    print(reverse('my_app:redirect_to_about'))
    return HttpResponseRedirect(reverse('my_app:redirect_to_about'))


def book_list(request):
    books = Book.objects.all()
    return render(request, 'my_app/book-list.html', {'books': list(books)})



def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'my_app/book-detail.html', {'book': book})