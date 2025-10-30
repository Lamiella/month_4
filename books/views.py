from django.shortcuts import render
from django.http import HttpResponse
import random
from datetime import datetime as dt


def about_me_view(request):
    if request.method == 'GET':
        return HttpResponse('1000-7')


def authors_random_view(request):
    if request.method == 'GET':
        blogs_random = ['Рукописи не горят!', 'Влюбиться можно в красоту, но полюбить — лишь только душу!',
                        'Разум бессилен перед криком сердца']
        return HttpResponse(random.choice(blogs_random))

def time_view(request):
    if request.method == "GET":
        time = dt.now()
        hour = time.strftime("%H")
        if 6 <= int(hour) <= 11:
            return HttpResponse('Сейчас утро')
        elif 12 <= int(hour) <= 14:
            return HttpResponse('Сейчас обед')
        elif 15<= int(hour) <= 20:
            return HttpResponse("Сейчас вечер")
        else:
            return HttpResponse("Сейчас ночь")
