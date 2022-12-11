from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import EmailForSending, GroupEmail, Message
from .forms import CreateGroupForEmailForm, EmailCreateForm, MessageForm

User = get_user_model()


class TestSendingEmailsApp(TestCase):
    """Тестирование приложения sending_emails"""

    def setUp(self) -> None:
        self.test_user = User.objects.create(
            email='test_user@email.com',
            username='test_user@email.com',
            first_name='test_user@email.com',
            last_name='test_user@email.com',
            password='awdawfawemail34567com',
        )
        self.test_user.save()

        self.email = EmailForSending(
            email='test_email@test.test',
            owner='test_user',
            user=self.test_user
        )
        self.email.save()

        self.test_group = GroupEmail(
            name='test_group',
            user=self.test_user
        )
        self.test_group.save()

    def test_get_anonymous_user(self):
        """Тестирование доступа анонимным пользователем"""

        URLS_LIST = [
            reverse('email:create_email'),
            reverse('email:create_group'),
            reverse('email:detail_email', kwargs={'pk': self.email.pk}),
        ]
        print(self.email.pk)
        for url in URLS_LIST:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 302)
        response = self.client.get(
            reverse('email:delete_email', kwargs={'pk': self.email.pk}))
        self.assertEqual(response.status_code, 404)

    def test_get_in_authenticated_user(self):
        """Тестирование доступа авторизованным пользователем"""

        URLS_LIST = [
            reverse('email:create_email'),
            reverse('email:create_group'),
            reverse('email:detail_email', kwargs={'pk': self.email.pk}),
        ]
        self.client.force_login(self.test_user)
        for url in URLS_LIST:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse('email:delete_email', kwargs={'pk': self.email.pk}))
        self.assertEqual(response.status_code, 302)

    def test_get_form_create_group_for_email(self):
        """Тестирование функции создания группы для электронной почты"""

        self.client.force_login(self.test_user)
        payload = {
            'name': 'test_group',
            'user': self.test_user
        }
        response_get = self.client.get(reverse('email:create_group'))
        self.assertIsInstance(response_get.context['form'],
                              CreateGroupForEmailForm)
        response_post = self.client.post(reverse('email:create_group'),
                                         data=payload)
        self.assertEqual(response_post.status_code, 302)

    def test_get_form_create_email(self):
        """Тестирование функции создания электронной почты"""

        self.client.force_login(self.test_user)
        payload = {
            'email': 'test_email@email.test',
            'owner': 'test_user',
            'user': self.test_user,
            'group': self.test_group.pk
        }
        response_get = self.client.get(reverse('email:create_email'))
        self.assertIsInstance(response_get.context['form'], EmailCreateForm)
        response_post = self.client.post(reverse('email:create_email'),
                                         data=payload)
        self.assertEqual(response_post.status_code, 302)

    def test_get_form_send_message(self):
        """Тестирование функции рассылки электронных писем"""

        self.client.force_login(self.test_user)
        path = reverse('email:detail_email', kwargs={'pk': self.email.pk})
        response_get = self.client.get(path)
        self.assertIsInstance(response_get.context['form'], MessageForm)

        message = Message.objects.create(
            text='test test test test test '
        )
        self.assertEqual(message.email.count(), 0)
        message.email.add(self.email)
        message.save()
        self.assertEqual(message.email.count(), 1)

    def test_error_post(self):
        """Тестирование возвращение ошибок при заполнении форм"""

        self.client.force_login(self.test_user)
        payload = {
            'name': ''
        }
        response = self.client.post(reverse('email:create_group'),
                                    data=payload)
        self.assertIn('name', response.context['form'].errors)
        payload = {
            'email': '',
            'owner': 'test_user',
            'user': self.test_user,
            'group': self.test_group.pk
        }
        response = self.client.post(reverse('email:create_email'),
                                    data=payload)
        self.assertIn('email', response.context['form'].errors)
