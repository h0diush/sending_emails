from django.contrib import messages
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, FormView, ListView

from apps.sending_emails.models import EmailForSending
from .forms import CreateGroupForEmailForm, EmailCreateForm, MessageForm
from .mixins import FormViewMixins
from .utils import send_message


class HomePage(ListView):
    template_name = 'index.html'
    context_object_name = 'emails'
    model = EmailForSending

    def get_queryset(self):
        if not self.request.user.is_anonymous:
            return self.request.user.emails_users.all()
        return None


class EmailCreateView(FormViewMixins):
    template_name = 'emails/create_email.html'
    form_class = EmailCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class CreateGroupForEmailView(FormViewMixins):
    template_name = 'emails/create_group.html'
    form_class = CreateGroupForEmailForm


class SendMessageEmailView(DetailView, FormView):
    template_name = 'emails/emails_detail.html'
    model = EmailForSending
    form_class = MessageForm
    context_object_name = 'email'
    success_url = '/'

    def form_valid(self, form):
        emails = form.save()
        emails.email.add(self.get_object())
        text = form.cleaned_data['text']
        emails = form.cleaned_data['email']
        send_message(emails, text)
        return super().form_valid(form)

    # def post(self, request, *args, **kwargs):

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class EmailDeleteView(DeleteView):
    model = EmailForSending
    success_url = reverse_lazy('email:index')

    def get(self, request, *args, **kwargs):
        messages.add_message(
            self.request, messages.INFO,
            f'Почта {self.get_object().email} успешна удалена'
        )
        return self.post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        obj = super(EmailDeleteView, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj
