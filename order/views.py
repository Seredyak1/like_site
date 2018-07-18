from django.shortcuts import render, get_object_or_404, redirect
from product.models import Journey
from .models import Order
from .forms import CreateOrder


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

            return render(request, 'product/Journey_card.html', {'form': form})

    else:

        return redirect("/")
