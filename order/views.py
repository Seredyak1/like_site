from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.cache import cache
from django.core.mail import send_mail
from likesite.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _

from product.models import Journey, Category
from .forms import CreateOrderAnonim, CreateCampOrder
from .models import Order
from camp.models import Camp, CampDates
from .tasks import send_order_anonim_email, send_order_email

def order_anonim(request):
    categories = Category.objects.all()
    """Create order anonim"""
    if request.method == "POST":
        form = CreateOrderAnonim(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("Ваше замовлення зареєстроване!"
                                      "Наш менеджер обов'язково Вас сконтактує найблищим часом!"))

            email = request.POST['email']
            send_order_anonim_email.delay(email)
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
            email = order.email_address
            send_order_email.delay(email)
            return render(request, 'order/confirmation_page.html', {'categories': categories})

        else:

            return render(request, 'order/order_for_users.html', {'journey': journey,
                                                                  'categories': categories,
                                                                  'cached_persons': cached_persons,
                                                                  'full_price': full_price})

    else:
        messages.error(extra_tags='danger', request=request, message=_('Для замовлення пригоди спочатку зареєструйтесь!'))
        return redirect('home')


def update_persons(request, journey_id):
    cache.set('persons', request.POST['update_persons'], 100)

    return redirect('/order/journey/{}'.format(journey_id))


def create_camp_order(request, slug):
    categories = Category.objects.all()
    camp = Camp.object.filter(slug=slug)
    if request.method == "POST":
        form = CreateCampOrder()
        form.fields['dates'].quesryset = CampDates.objects.filter(camp=camp)
        if form.is_valid():
            form.save()
            messages.success(request, _("Ваше замовлення зареєстроване!"
                                      "Наш менеджер обов'язково Вас сконтактує найблищим часом!"))

            send_mail(_('LAIK TRAVEL - пітвердження замовлення'),
                      '',
                      EMAIL_HOST_USER,
                      [request.POST['email']],
                      html_message=render_to_string('order/email_confirmation.html'),
                      fail_silently=False)

            send_mail('LAIK TRAVEL - замовлення',
                      """Зробили нове анонімне замовлення! Зконтактувати найблищим часом. 
                      http://laik-travel.com/admin/order/order/
                      """,
                      EMAIL_HOST_USER,
                      ['sanya.seredyak@gmail.com', 'office@laik-travel.com'],
                      fail_silently=False)

            redirect('/')

    form = CreateCampOrder()
    return render(request, 'order/order_for_camp.html', {'form': form, 'categories': categories})
