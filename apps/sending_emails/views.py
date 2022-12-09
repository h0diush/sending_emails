from django.views.generic import FormView, ListView

from apps.sending_emails.models import EmailForSending
from .forms import EmailCreateForm, CreateGroupForEmailForm


class HomePage(ListView):
    template_name = 'index.html'
    context_object_name = 'emails'
    model = EmailForSending

    def get_queryset(self):
        if not self.request.user.is_anonymous:
            return self.request.user.emails_users.all()
        return None


class EmailCreateView(FormView):
    template_name = 'emails/create_email.html'
    form_class = EmailCreateForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class CreateGroupForEmailView(FormView):
    template_name = 'emails/create_group.html'
    form_class = CreateGroupForEmailForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
