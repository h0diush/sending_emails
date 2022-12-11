from django.contrib.auth import get_user_model
from django.core import mail
from django.test import TestCase
from django.urls import reverse

from .forms import PasswordResetForm, RegisterForm

User = get_user_model()


class TestUserCreate(TestCase):
    """Тестирование регистрации пользователя"""

    def setUp(self) -> None:
        self.test_user = User.objects.create(
            email='test_user@email.com',
            username='test_user@email.com',
            first_name='test_user@email.com',
            last_name='test_user@email.com',
            password='awdawfawemail34567com',
        )
        self.test_user.save()

    def test_get(self):
        """Тестируем доступ страницы с регистрацией"""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], RegisterForm)

    def test_post(self):
        """Тестируем регистрацию пользователя"""
        email = 'test@email.com'
        payload = {
            'username': 'username',
            'last_name': 'username',
            'first_name': 'username',
            'email': email,
            'password1': 'akwjdhkjaw234',
            'password2': 'akwjdhkjaw234'
        }
        response = self.client.post(reverse('register'), data=payload)
        self.assertEqual(response.status_code, 302)
        # self.assertEqual(mail.outbox, email)
        user = User.objects.filter(email=email).first()
        self.assertEqual(user.email, email)
        self.assertTrue(user.is_authenticated)

    def test_post_error(self):
        """Тестируем ошибки при регистрации формы"""

        error_email_msg = '* Пользователь с test_user@email.com уже существует'
        error_username_msg = \
            '* Пользователь с никнеймом test_user@email.com уже существует'
        email = self.test_user.email
        username = self.test_user.username
        payload = {
            'username': username,
            'email': email,
            'first_name': 'test',
            'last_name': 'test',
            'password1': 'akwjdhkjaw234',
        }
        response = self.client.post(reverse('register'), data=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], RegisterForm)
        self.assertIn('password2', response.context['form'].errors)
        self.assertIn('email', response.context['form'].errors)
        self.assertIn('username', response.context['form'].errors)
        self.assertEqual(
            response.context['form'].errors['email'].as_text(),
            error_email_msg
        )
        self.assertEqual(
            response.context['form'].errors['username'].as_text(),
            error_username_msg
        )

    def _test_reset_password(self, email):
        payload = {
            'email': email
        }
        return self.client.post(reverse('password_reset'), payload)

    def test_password_reset(self):
        """Тестируем страницу с восстановлением пароля"""

        email = 'test_user@email.com'
        response = self._test_reset_password(email)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(''.join(mail.outbox[0].to), email)
        self.assertEqual(response.status_code, 302)
        response = self._test_reset_password('test_usb2@email.com')
        text_error = '* Почта test_usb2@email.com не зарегистрирована на сайте'
        self.assertEqual(response.status_code, 200)
        self.assertIn('email', response.context['form'].errors)
        self.assertEqual(
            response.context['form'].errors['email'].as_text(),
            text_error
        )
        self.assertIsInstance(response.context['form'], PasswordResetForm)
