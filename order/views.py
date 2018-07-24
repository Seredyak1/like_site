from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Order
from product.models import Journey
from product.models import Category
from .forms import CreateOrderAnonim


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
        order = Order.objects.filter().last()

        if journey.sale_price:
            full_price = order.persons * journey.sale_price
        else:
            full_price = order.persons * journey.price

        if request.method == "POST":
            order, created = Order.objects.get_or_create(user=request.user, journey=journey,
                                                         contact_phone=request.POST['contact_phone'],
                                                         persons=order.persons,
                                                         total=full_price)
            order.save()

            return redirect('/')

        else:

            return render(request, 'order/order_for_users.html', {'journey': journey,
                                                                  'categories': categories, 'order': order,
                                                                  'full_price': full_price})

    else:
        return redirect("/")


def update_persons(request, journey_id):
    order = Order.objects.filter().last()
    order.persons = request.POST['update_persons']
    order.save()

    return redirect('/order/journey/{}'.format(journey_id))
