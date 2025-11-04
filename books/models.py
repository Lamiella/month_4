from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    GENRE = (
        ('Фантастика', 'Фантастика'),
        ('Ужасы', 'Ужасы'),
        ('Драма', 'Драма'),
        ('Роман', 'Роман'),
        ('Фэнтези', 'Фэнтези'),
        ('История', 'История'),
    )

    title = models.CharField(max_length=100, verbose_name='Укажите название книги')
    image = models.ImageField(upload_to='books/', verbose_name='Загрузите обложку')
    description = models.TextField(verbose_name='Укажите аннотацию')
    director = models.CharField(max_length=100, verbose_name='Укажите автора книги', default='Иванов Иван')
    genre = models.CharField(max_length=100, choices=GENRE, verbose_name='Укажите жанр')
    country = models.CharField(max_length=100, default='США', verbose_name='Укажите страну')
    pages = models.PositiveIntegerField(verbose_name='Укажите количество страниц', default=400)
    age = models.PositiveIntegerField(verbose_name='Укажите возрастное ограничение', default=16)
    language = models.CharField(max_length=100, verbose_name='Укажите язык написания')
    publishing_house = models.CharField(max_length=100, verbose_name='Укажите издательство')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

class Reviews(models.Model):
    MARK = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5')
    )
    choice_book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    name_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    mark = models.CharField(max_length=100, choices=MARK, default='4')
    comments = models.TextField()

    def __str__(self):
        return f'{self.choice_book}-{self.mark}'