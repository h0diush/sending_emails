from django.contrib import messages
from django.contrib.auth import get_user_model, logout, views
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import TemplateView
from registration.backends.default.views import RegistrationView

from .forms import PasswordResetForm, RegisterForm

User = get_user_model()


class RegistrationUserView(RegistrationView):
    """Регистрация пользователей"""

    form_class = RegisterForm
    template_name = 'users/register.html'

    # success_url = reverse('index')

    def get_success_url(self, user=None):
        return reverse('email:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO,
            'Электронное письмо для подтверждения аккаунта успешно отправлено'
        )
        return super().form_valid(form)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


class ActivationEmailComplete(TemplateView):
    """Подтверждение электронной почты"""

    template_name = 'registration/activation_completed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Почта активирована'
        return context


class PasswordResetView(views.PasswordResetView):
    """Проверка перед восстановлением пароля,
       существует есть ли email в бд """

    form_class = PasswordResetForm


class PasswordChange(views.PasswordChangeView):
    """Изменение пароля"""

    title = 'Изменение пароля'


class LoginUserView(LoginView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход'
        return context
