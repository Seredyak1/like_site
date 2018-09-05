from django.shortcuts import render
from product.models import Journey, Category
from pages.models import Feedback, ClientCompany
from news.models import News


def home(request):
    journeys = Journey.objects.all()[:8]
    feedbacks = Feedback.objects.all().exclude(is_published=False)[:5]
    newses = News.objects.last()
    categories = Category.objects.all()
    clients = ClientCompany.objects.all()
    return render(request, 'landing_page/home.html', {'journeys': journeys,
                                                      'feedbacks': feedbacks,
                                                      'newses': newses,
                                                      'categories': categories,
                                                      'clients': clients})
