from django.views.generic import FormView
from django import forms


class FormViewMixins(FormView):
    """Миксин для обработки форм"""
    # form_class = None
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
