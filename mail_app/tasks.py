from celery import shared_task
from django.core.mail import send_mail
from MyCeleryProject import settings
@shared_task(bind=True)
def mail_func(self):
    # operation
    users = ["supritk16@gmail.com","supritkumar00@gmail.com","xarvismark@gmail.com","supritkumar98@gmail.com","sshipu98@gmail.com"]
    for user in users:
        mail_subject = "Hi! Celery Testing"
        message = "This is a Celery Testing mail. Please ignore this."
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user],
            fail_silently=True,
        )
    return "Mail Sent"