from django.conf import settings
from django.core.mail import EmailMessage


def send_email_to(subject, email, html_body=None):
    """
    Send email to given address
    """
    email = EmailMessage(
        subject=subject,
        body=html_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[email]
    )
    email.content_subtype = 'html'
    email.send()
