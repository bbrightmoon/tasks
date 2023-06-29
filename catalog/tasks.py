from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from celery import shared_task

from catalog.models import Product
from project0.settings.env_reader import env


@shared_task(bind=True)
def send_promotional_emails(self):
    users = get_user_model().objects.all()
    products_w_discount = Product.objects.filter(discount=True).order_by('id').values_list('title')
    list_of_products = list(products_w_discount)
    for user in users:
        mail_subject = "Discount!"
        message = f"The list of products with discount: {list_of_products}"
        to_email = user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=env('EMAIL_HOST_USER'),
            recipient_list=[to_email]
        )
    return "Task is successful"









