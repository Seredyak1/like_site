import logging
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _

from likesite.settings import EMAIL_HOST_USER
from .celery import app

@app.task
def send_order_anonim_email(email):

    send_mail(_('LAIK TRAVEL - пітвердження замовлення'),
                  '',
                  EMAIL_HOST_USER,
                  (email,),
                  html_message=render_to_string('order/email_confirmation.html'),
                  fail_silently=False)

    send_mail('LAIK TRAVEL - замовлення',
                  """Зробили нове анонімне замовлення! Зконтактувати найблищим часом. 
                  http://laik-travel.com/admin/order/order/
                  """,
                  EMAIL_HOST_USER,
                  ['sanya.seredyak@gmail.com', 'office@laik-travel.com'],
                  fail_silently=False)

@app.task
def send_order_email(email):
    try:
        send_mail(_('LAIK TRAVEL - пітвердження замовлення'),
                  '',
                  EMAIL_HOST_USER,
                  (email,),
                  html_message=render_to_string('order/email_confirmation.html'),
                  fail_silently=False)

        send_mail('LAIK TRAVEL - замовлення',
                  """Зробили нове замовлення! Зконтактувати найблищим часом. 
                  http://laik-travel.com/admin/order/orderanonim/
                  """,
                  EMAIL_HOST_USER,
                  ['sanya.seredyak@gmail.com', 'office@laik-travel.com'],
                  fail_silently=False)
    except:
        logging.warning("Email don't works")
