from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):

    QUALIFICATION = (
        ('junior', 'junior'),
        ('senior', 'senior'),
        ('middle', 'middle'),
    )

    GENDER = (
        ('male', 'male'),
        ('female', 'female'),
    )

    IT_LANGUAGES =(
        ('python', 'python'),
        ('java', 'java'),
        ('ruby', 'ruby'),
    )

    LANGUAGES = (
        ('English', 'English'),
        ('French', 'French'),
        ('Italian', 'Italian'),
        ('Russian', 'Russian'),
    )

    phone_number = models.CharField(max_length=13)
    gender = models.CharField(max_length=100, choices=GENDER)
    birth_date = models.DateField()
    it_languages = models.CharField(max_length=100, choices=IT_LANGUAGES)
    languages = models.CharField(max_length=100, choices=LANGUAGES)
    qualification = models.CharField(max_length=100, choices=QUALIFICATION)


    def __str__(self):
        return self.username