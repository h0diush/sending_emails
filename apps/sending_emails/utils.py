from django.core.mail import EmailMultiAlternatives


def send_message(emails, text):
    """Утилита для отправки электронных писем"""

    EMAILS = []
    for email in emails:
        EMAILS.append(email.email)
    msg = EmailMultiAlternatives(subject='HELLO', to=EMAILS)
    msg.attach_alternative(text, 'text/html')
    msg.send()
