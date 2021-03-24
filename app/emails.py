from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template


def send_email(subject, message, recipient_list=None):

    email_from = settings.EMAIL_HOST_USER
    template = get_template('send_email_test.html')
    send_mail(subject, message, email_from, recipient_list,
              html_message=template.render(context={
                  'message': message,
              }))
