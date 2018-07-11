from django.shortcuts import render, get_object_or_404
from product.models import Category, Journey
from product.utils import handle_pagination


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    categories = Category.objects.all()
    journeys = Journey.objects.filter(category=category)
    journeys_with_sale = Journey.objects.filter(category=category).exclude(sale_price__isnull=True)[:5]
    return render(request, 'product/Category_detail.html', {'category': category,
                                                            'categories': categories,
                                                            'journeys': handle_pagination(request, journeys),
                                                            'journeys_with_sale': journeys_with_sale})
