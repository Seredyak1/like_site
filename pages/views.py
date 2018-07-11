from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render

from pages.forms import FeedbackForm
from pages.models import Feedback
from product.models import Category

def feedback(request):
    """Create or show list for feedback"""
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваш відгук буде опубліковано після перевірки модератором. Дякуємо!')

    form = FeedbackForm()

    feedbacks = Paginator(Feedback.objects.exclude(is_published=False), 10)
    page = request.GET.get('page')
    feedbacks = feedbacks.get_page(page)

    return render(request, 'pages/feedback.html', {'feedbacks': feedbacks, 'form': form})


def about_us(request):
    categories = Category.objects.all()
    return render(request, 'pages/about_us.html', {"categories": categories})
