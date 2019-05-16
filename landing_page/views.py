from django.shortcuts import render
from django.views import View

from product.models import Journey, Category
from pages.models import Feedback, ClientCompany
from news.models import News


class LandingPageView(View):

    template_name = 'landing_page/home.html'

    def get(self, request, *args, **kwargs):
        journeys = Journey.objects.all()[:12]
        feedbacks = Feedback.objects.all().exclude(is_published=False)[:5]
        newses = News.objects.first()
        categories = Category.objects.all()
        clients = ClientCompany.objects.all()
        return render(request, 'landing_page/home.html', {'journeys': journeys,
                                                          'feedbacks': feedbacks,
                                                          'newses': newses,
                                                          'categories': categories,
                                                          'clients': clients})
