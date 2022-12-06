from django.db import models
from django.urls.base import reverse
from django.utils.translation import gettext_lazy as _


class GroupEmail(models.Model):
    """Группы электронных писем"""

    name = models.CharField(_('Название'), max_length=55)

    class Meta:
        verbose_name = 'Группа для электронной почты'
        verbose_name_plural = 'Группы для электронной почты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('group', kwargs={'pk': self.pk})


class EmailForSending(models.Model):
    """Электронные письма"""

    email = models.EmailField(
        _("Электронная почта"),
        max_length=35, unique=False,
    )
    owner = models.CharField(
        _("Владелец почты"), max_length=155,
        null=True, blank=True
    )
    created = models.DateField(_('Дата создания'), auto_now_add=True)
    group = models.ForeignKey(
        "sending_emails.GroupEmail",
        verbose_name='Группа',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Электронная почта'
        verbose_name_plural = 'Электронные почты'
        ordering = ['-created']

    def __str__(self):
        return f'{self.email} ---> {self.owner}'

    def get_absolute_url(self):
        return reverse('email_for_sending', kwargs={'pk': self.pk})


class Message(models.Model):
    """Модель отправки электронных писем"""

    email = models.ManyToManyField(
        to='sending_emails.EmailForSending', related_name='emails',
        verbose_name='Электронные почты'
    )
    text = models.TextField(_("Текст"))
    created = models.DateField(_('Дата создания'), auto_now_add=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщении'
        ordering = ['-created']

    def __str__(self):
        return f'{self.email}, Отправлено: {self.created}'

    def get_absolute_url(self):
        return reverse('message', kwargs={'pk': self.pk})
