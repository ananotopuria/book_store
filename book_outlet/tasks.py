from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_welcome_email(email):
    subject = 'Welcome to our platform!'
    message = 'Thank you for registering.'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    
    send_mail(subject, message, from_email, recipient_list)
    
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
import random

@shared_task
def send_weekly_newsletter():
    
    subject = 'Weekly Newsletter'
    message = 'Here is your randomly generated newsletter content: {}'.format(random.randint(1, 100))
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = ['recipient@example.com']
    
    send_mail(subject, message, from_email, recipient_list)