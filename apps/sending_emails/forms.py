from ckeditor.widgets import CKEditorWidget
from django import forms

from apps.sending_emails.models import EmailForSending, Message


class MessageForm(forms.ModelForm):
    """Форма создания электронного письма"""

    email = forms.ModelMultipleChoiceField(
        widget=forms.SelectMultiple, queryset=EmailForSending.objects.all()
    )
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Message
        fields = ('email', 'text')
