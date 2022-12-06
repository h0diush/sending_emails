from django.contrib import admin

from .forms import MessageForm
from .models import EmailForSending, GroupEmail, Message


@admin.register(EmailForSending)
class EmailForSendingAdmin(admin.ModelAdmin):
    """Админ панель для электронных писем"""

    list_display = ('owner', 'email', 'group', 'created')
    list_filter = ('owner', 'group')
    list_display_links = ('owner',)


@admin.register(GroupEmail)
class GroupEmail(admin.ModelAdmin):
    """Админ панель для группировки электронных писем"""

    list_display = ('name',)
    list_display_links = ('name',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Админ панель для отправки электронных писем"""

    list_display = ('created',)
    # list_display_links = ('email',)
    form = MessageForm
