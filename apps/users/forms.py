from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordResetForm as ResetForm

from .models import User


class RegisterForm(UserCreationForm):
    """Форма регистрации пользователя"""

    username = forms.CharField(label='Никнейм', widget=forms.TextInput())
    email = forms.EmailField(
        label='Электронная почта', widget=forms.EmailInput())
    first_name = forms.CharField(label='Имя', widget=forms.TextInput())
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput())
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(
        label='Повторите пароль', widget=forms.PasswordInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name',
        )

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                f'Пользователь с {email} уже существует')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                f'Пользователь с никнеймом {username} уже существует')
        return username

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError('Пароли не совпадают')
        return password2


class PasswordResetForm(ResetForm):
    """Форма валидации электронной почты,
     существует ли пользователь в бд, для восстановления пароля"""

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                f'Почта {email} не зарегистрирована на сайте')
        return email
