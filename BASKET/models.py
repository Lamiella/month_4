from django.db import models
from books.models import Book

class Order(models.Model):
    PAYMENT = (
        ('Карта', 'Карта'),
        ('Наличные', 'Наличные'),
        ('QR-код', 'QR-код'),
    )

    address = models.CharField(max_length=100, verbose_name='Укажите адрес')
    inn = models.CharField(max_length=100, verbose_name='Укажите ИНН')
    payment = models.TextField(max_length=100, choices=PAYMENT, verbose_name='Укажите способ оплаты')
    books = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')