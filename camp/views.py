from django.shortcuts import render

from .models import Camp, CampComment
from product.models import Category


def get_camp_page(request):
    categories = Category.objects.all()
    camps = Camp.object.all()
    return render(request, 'camp/home_camp_page.html', {'camps': camps,
                                                        'categories': categories})
