from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField

QUALIFICATION = (
    ('junior', 'junior'),
    ('senior', 'senior'),
    ('middle', 'middle'),
)

GENDER = (
    ('male', 'male'),
    ('female', 'female'),
)

IT_LANGUAGES = (
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

class LoginForm(AuthenticationForm):
    captcha = CaptchaField()

class CustomRegisterForm(UserCreationForm):
    phone_number = forms.CharField(max_length=13, required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    birth_date = forms.DateField(required=True)
    it_languages = forms.ChoiceField(choices=IT_LANGUAGES, required=True)
    languages = forms.ChoiceField(choices=LANGUAGES, required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    qualification = forms.ChoiceField(choices=QUALIFICATION, required=True)
    captcha = CaptchaField()

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'password1',
            'password2',
            'email',
            'first_name',
            'last_name',
            'gender',
            'phone_number',
            'gender',
            'birth_date',
            'it_languages',
            'languages',
            'qualification',
        )

        def save(self, commit=True):
            user = super(CustomRegisterForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user