from django.contrib.auth import get_user_model
from django.core.mail import send_mail,EmailMessage
from django_celery_project import settings

from celery import shared_task


@shared_task(bind=True,name='send_email_repatly')
def send_email_func(self):
    users = get_user_model().objects.all()
    for user in users:
        mail_subject = 'Hello! Celery and Redis'
        message = 'If you using celery,Permissible You'
        to_email = user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list = [to_email],
            fail_silently=True
        )
    return 'Done.Successfully Sending Gmail'

