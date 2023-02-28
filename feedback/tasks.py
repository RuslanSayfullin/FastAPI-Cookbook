from time import sleep

from celery import shared_task
from django.core.mail import send_mail


@shared_task()
def send_feedback_email_task(email_address, message):
    """Sends an email when the feedback form has been submitted."""
    sleep(20)  # Simulate expensive operation(s) that freeze Django
    send_mail(
        "Ваш отзыв",
        f"\t{message}\n\nСпасибо!",
        "ruslansaifullin91@gmail.com",
        [email_address],
        fail_silently=False,
    )
