from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm

from loginsys.models import UserProfile

class registrationsForm(UserCreationForm):
    username=forms.CharField(
        label='Никнейм:*',
        help_text='',
        max_length=50,
        required=True,
    )
    first_name = forms.CharField(
        label='Имя:*',
        help_text='',
        max_length=50,
        required=True,
    )
    last_name = forms.CharField(
        label='Фамилия:*',
        help_text='',
        max_length=50,
        required=True,
    )

    '''
    phone = forms.CharField(
        label='Телефон:*',
        help_text='',
        max_length=50,
        required=True,
    )
    '''
    password1 = forms.CharField(
        label='Пароль:*',
        help_text='',
        required=True,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label='Подтверждение пароля:*',
        help_text='',
        required=True,
        widget=forms.PasswordInput,
    )

    email = forms.CharField(
        label='Email:*',
        help_text='Максимальная длина 13 символов',
        required=True
    )


    class Meta:
        model = UserProfile
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'email']#'phone'