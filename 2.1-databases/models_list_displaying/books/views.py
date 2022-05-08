from django.shortcuts import render
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books_query = Book.objects.all()
    context = {'books': books_query}
    return render(request, template, context)


def books_date_view(request, date):
    template = 'books/books_list.html'
    books_query = Book.objects.filter(pub_date=date)
    prev_p = Book.objects.filter(pub_date__lt=date).order_by('pub_date')
    next_p = Book.objects.filter(pub_date__gt=date).order_by('pub_date')
    if prev_p.count() > 0:
        prev_page = prev_p[prev_p.count() - 1].pub_date.strftime("%Y-%m-%d")
    else:
        prev_page = None
    if next_p.count() > 0:
        next_page = next_p[0].pub_date.strftime("%Y-%m-%d")
    else:
        next_page = None

    context = {'books': books_query,
               'prev_page_url': prev_page,
               'next_page_url': next_page,
               }
    return render(request, template, context)
