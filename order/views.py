from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Order
from product.models import Journey
from product.models import Category
from .forms import CreateOrderAnonim, CreateOrder


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
    categories = Category.objects.all()
    if request.user.is_authenticated:
        journey = get_object_or_404(Journey, id=journey_id)

        if request.method == "POST":

            Order.objects.create(user=request.user, journey=journey, contact_phone=request.POST['contact_phone'],
                                 persons=request.POST['persons'], total=int(request.POST['persons']) * journey.price)

            return render(request, 'product/Journey_card.html')

        else:

            form = CreateOrder()
            return render(request, 'order/order.html', {'form': form, 'journey': journey, 'categories':categories})

    else:
        return redirect("/")
