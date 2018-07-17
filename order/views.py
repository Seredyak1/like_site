from django.shortcuts import render, redirect
from django.contrib import messages


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
