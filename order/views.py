from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Order
from product.models import Journey
from product.models import Category
from .forms import CreateOrderAnonim
from django.core.cache import cache


def order_anonim(request):
    categories = Category.objects.all()
    """Create order anonim"""
    if request.method == "POST":
        form = CreateOrderAnonim(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ваше замовлення зареєстроване!"
                                      " Наш менеджер обов'язково Вас сконтактує найблищим часом!")
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
                                                         email_address=request.user.email,
                                                         contact_phone=request.POST['contact_phone'],
                                                         persons=cached_persons,
                                                         total=full_price)
            order.save()

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
