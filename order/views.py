from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from product.models import Category
from .forms import CreateOrderAnonim, CreateOrder
from .models import Order
from product.models import Journey
from product.models import Category
from .models import OrderAnonim
from .forms import CreateOrderAnonim


def order_anonim(request):
    categories = Category.objects.all()
    """Create order anonim"""
    if request.method == "POST":
        form = CreateOrderAnonim(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ваше замовлення зареєстроване! Наш менеджер обов'язково Вас сконтактує найблищим часом!")
            redirect('/')

    form = CreateOrderAnonim()

    return render(request, 'order/order_for_anonim.html', {'form': form, 'categories': categories})


def create_order(request, journey_id):
    if request.user.is_authenticated:
        journey = get_object_or_404(Journey, journey_id)

        if request.method == "POST":
            order = Order.objects.create(user=request.user, total=journey.price,
                                         contact_phone=request.POST['contact_phone'],
                                         journey=journey_id)

            form = CreateOrder(request.POST, instance=order)
            if form.is_valid():
                form.save()

            return render(request, 'product/Journey_card.html', {'form': form, 'journey': journey})

    else:

        return redirect("/")