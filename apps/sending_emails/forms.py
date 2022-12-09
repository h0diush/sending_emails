from ckeditor.widgets import CKEditorWidget
from django import forms

from apps.sending_emails.models import EmailForSending, Message, GroupEmail


class MessageForm(forms.ModelForm):
    """Форма создания электронного письма"""

    email = forms.ModelMultipleChoiceField(
        widget=forms.SelectMultiple, queryset=EmailForSending.objects.all()
    )
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Message
        fields = ('email', 'text')


class EmailCreateForm(forms.ModelForm):
    """Форма для добавления почты """

    def __init__(self, *args, **kwargs):
        """Метод, который отбирает группы одного пользователя """

        user = kwargs.pop('user', None)
        super(EmailCreateForm, self).__init__(*args, **kwargs)
        groups = user.groups_users.all()
        if groups:
            self.fields['group'].queryset = user.groups_users.all()
        else:
            del self.fields['group']

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
