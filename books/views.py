from django.shortcuts import render, get_object_or_404
from . import models
from django.db.models import Avg


#detailView
def bookDetailView(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Book, id=id)
        average_rating = models.Reviews.objects.filter(choice_book=book_id).aggregate(Avg('mark'))['mark__avg']
        context = {
            'book_id': book_id,
            'average_rating': round(average_rating, 1)
        }
    return render(request, template_name='books/book_detail.html', context=context)


#listView
def bookListView(request):
    if request.method == 'GET':
        book = models.Book.objects.all()
        context = {
            'book': book
        }
    return render(request, template_name='books/book.html', context=context)