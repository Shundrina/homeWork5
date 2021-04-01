from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template


def send_email(recipient_list=None, activate_url=None):

    email_from = settings.EMAIL_HOST_USER
    subject = 'some subject'
    message = 'some message'
    template = get_template('send_email_test.html')
    send_mail(subject, message, email_from, recipient_list,
              html_message=template.render(context={
                  'message': message,
                  'activate_url': activate_url,
              }))
