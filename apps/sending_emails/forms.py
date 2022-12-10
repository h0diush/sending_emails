from ckeditor.widgets import CKEditorWidget
from django import forms

from apps.sending_emails.models import EmailForSending, GroupEmail, Message
from .mixins import FormModelMixin


class MessageForm(FormModelMixin):
    """Форма создания электронного письма"""

    email = forms.ModelMultipleChoiceField(label='Электронные почты:',
                                           widget=forms.SelectMultiple,
                                           queryset=None
                                           )
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Message
        fields = ('email', 'text')


class EmailCreateForm(FormModelMixin):
    """Форма для добавления почты """

    group = forms.ModelChoiceField(label='Группа', widget=forms.Select(),
                                   queryset=None, required=False)

    class Meta:
        model = EmailForSending
        fields = ('email', 'owner', 'group')


class CreateGroupForEmailForm(forms.ModelForm):
    """Форма для создания групп электронных почт"""

    class Meta:
        model = GroupEmail
        fields = ('name',)
