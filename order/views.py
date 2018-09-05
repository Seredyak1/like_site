from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Order
from product.models import Journey, Category
from .forms import CreateOrderAnonim
from django.core.cache import cache
from django.core.mail import send_mail
from likesite.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string


def order_anonim(request):
    categories = Category.objects.all()
    """Create order anonim"""
    if request.method == "POST":
        form = CreateOrderAnonim(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ваше замовлення зареєстроване!"
                                      " Наш менеджер обов'язково Вас сконтактує найблищим часом!")

            send_mail('LAIK TRAVEL - пітвердження замовлення',
                      '',
                      EMAIL_HOST_USER,
                      [request.POST['email']],
                      html_message=render_to_string('order/email_confirmation.html'),
                      fail_silently=False)

            send_mail('LAIK TRAVEL - замовлення',
                      """Зробили нове анонімне замовлення! Зконтактувати найблищим часом. 
                      http://127.0.0.1:8000/admin/order/orderanonim/
                      """,
                      EMAIL_HOST_USER,
                      ['sanya.seredyak@gmail.com', 'avseredyak@gmail.com', 'office@laik-travel.com'],
                      fail_silently=False)

            redirect('/')

    form = CreateOrderAnonim()

    return render(request, 'order/order_for_anonim.html', {'form': form, 'categories': categories})


def create_order(request, journey_id):
    categories = Category.objects.all()

    if request.user.is_authenticated:
        journey = get_object_or_404(Journey, id=journey_id)

        cached_persons = cache.get('persons', 1)

        if journey.sale_price:
            full_price = int(cached_persons) * journey.sale_price
        else:
            full_price = int(cached_persons) * journey.price

        if request.method == "POST":
            order, created = Order.objects.get_or_create(user=request.user, journey=journey,
                                                         email_address = request.user.email,
                                                         contact_phone=request.POST['contact_phone'],
                                                         persons=cached_persons,
                                                         total=full_price)
            order.save()

            send_mail('Here will be title of email!',
                      'Here is a text for email!!',
                      EMAIL_HOST_USER,
                      [order.email_address],
                      html_message=render_to_string('order/email_confirmation.html'),
                      fail_silently=False)

            send_mail('LAIK TRAVEL - замовлення',
                      """Зробили нове замовлення! Зконтактувати найблищим часом. 
                      http://127.0.0.1:8000/admin/order/order/
                      """,
                      EMAIL_HOST_USER,
                      ['sanya.seredyak@gmail.com', 'avseredyak@gmail.com', 'office@laik-travel.com'],
                      fail_silently=False)

            return render(request, 'order/confirmation_page.html')

        else:

            return render(request, 'order/order_for_users.html', {'journey': journey,
                                                                  'categories': categories,
                                                                  'cached_persons': cached_persons,
                                                                  'full_price': full_price})

    else:
        return redirect("/")


def update_persons(request, journey_id):
    cache.set('persons', request.POST['update_persons'], 100)

    return redirect('/order/journey/{}'.format(journey_id))
