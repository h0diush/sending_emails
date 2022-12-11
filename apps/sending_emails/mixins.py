from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView


class FormViewMixins(LoginRequiredMixin, FormView):
    """Миксин для обработки форм"""
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class FormModelMixin(forms.ModelForm):
    """Миксин для отображения форм"""

    def __init__(self, *args, **kwargs):
        """Метод, который отбирает группы одного пользователя """

        user = kwargs.pop('user', None)
        super(FormModelMixin, self).__init__(*args, **kwargs)
        try:
            groups = user.groups_users.all()
            if groups:
                self.fields['group'].queryset = groups
            else:
                del self.fields['group']
        except KeyError:
            emails = user.emails_users.all()
            if emails:
                self.fields['email'].queryset = emails
            else:
                del self.fields['email']
