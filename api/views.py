from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, views
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt

from .serializers import *
from .permissions import IsOwner


class CSRFExemptMixin(object):
   @method_decorator(csrf_exempt)
   def dispatch(self, *args, **kwargs):
       return super(CSRFExemptMixin, self).dispatch(*args, **kwargs)


# NEWS API VIEWS-----------------------------------------------------------------------------------------------
class NewsAPIView(generics.ListAPIView):
    """
    list:
    Return a list of all news
    """
    serializer_class = NewsPreviewSerializer

    def get_queryset(self):
        return News.objects.all().exclude(published=False)


class NewsDetailAPIView(generics.RetrieveAPIView):
    """
    get:
    Return one News obj by id
    """
    serializer_class = NewsSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return News.objects.all().exclude(published=False)


# PAGES API VIEWS-----------------------------------------------------------------------------------------------
class ClientCompanyAPIViews(generics.ListAPIView):
    """
    get:
    Return all companies
    """
    serializer_class = ClientCompanySerializer
    queryset = ClientCompany.objects.all()


class DocumentsApiView(generics.ListAPIView):
    """
    get:
    Return all documents
    """
    serializer_class = DocumentsSerializer
    queryset = Document.objects.all()


class FaqAPIView(generics.ListAPIView):
    """
    get:
    Return all FAQs
    """
    serializer_class = FAQSerializer

    def get_queryset(self):
        return Faq.objects.all()


class FeedbackAPIView(generics.ListCreateAPIView):
    """
    get:
    List with all feedback

    post:
    Create one new feedback
    """
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()

    def get_queryset(self):
        return Feedback.objects.all().exclude(is_published=False)


# CAMP API VIEWS ----------------------------------------------------------------------------------------------
class CampsAPIView(generics.ListAPIView):
    """
    get:
    List with all camps
    """
    serializer_class = CampPreviewSerializer

    def get_queryset(self):
        return Camp.object.all()


class CampDetailAPIView(generics.RetrieveAPIView):
    """
    get:
    Return one Camp obj by slug
    """
    serializer_class = CampDetailSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Camp.object.all()

class CampCommentsAPIView(generics.ListCreateAPIView):
    """
    post:
    Create new camp comment with auth user

    get:
    Return all comment for this Camp
    """
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CampCommentSerializer
    queryset = CampComment.objects.all()
    lookup_field = 'slug'

    def get_queryset(self):
        return CampComment.objects.filter(camp__slug=self.kwargs['slug'])

    def perform_create(self, serializer):
        camp = Camp.object.get(slug=self.kwargs['slug'])
        serializer.save(user=self.request.user, camp=camp)


class CampCommentUpdateOrDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    """

    """
    permission_classes = (IsOwner,)
    serializer_class = CampCommentSerializer
    queryset = CampComment.objects.all()
    lookup_field = 'id'


# PRODUCT API--------------------------------------------------------------------------------------------------

class CategoryListAPIView(generics.ListAPIView):
    """
    get:
    Return list of categories
    """
    serializer_class = CategoryListSerializer

    def get_queryset(self):
        return Category.objects.all()


class CategoryDetailAPIView(generics.RetrieveAPIView):
    """
    get:
    Return one Category by slug
    """
    serializer_class = CategoryDetailSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Category.objects.all()

class JourneyCardListAPIView(generics.ListAPIView):
    """
    get:
    Return list with all journeys
    """
    serializer_class = JourneyCardSerializer

    def get_queryset(self):
        return Journey.objects.all()[:10]


class JourneyCardListWithCategoryAPIView(generics.ListAPIView):
    """
    get:
    Return list with journeys by category
    """
    serializer_class = JourneyCardSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Journey.objects.filter(category__slug=self.kwargs['slug'])


class JourneyCardListForNewAPIView(generics.ListAPIView):
    """
    get:
    Return list with 10th first journies
    """
    serializer_class = JourneyCardSerializer

    def get_queryset(self):
        return Journey.objects.all().order_by("created_at")[:10]


class JourneyCardListWithSalePriceAPIView(generics.ListAPIView):
    """
    get:
    Return list with journeys with sale price
    """
    serializer_class = JourneyCardSerializer

    def get_queryset(self):
        return Journey.objects.all().exclude(sale_price__isnull=True)


class JourneyDetailAPIView(generics.RetrieveAPIView):
    """
    get:
    Return one journey by id
    """
    serializer_class = JourneySerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Journey.objects.all()


class JourneyCommentsAPIView(generics.ListCreateAPIView):
    """
    post:
    Create new journey comment by user id and journey id

    get:
    Return list with comments for one journey by id
    """
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = JourneyCommentsSerializer
    queryset = Comment.objects.all()
    lookup_field = 'journey_id'

    def get_queryset(self):
        return Comment.objects.filter(journey__id=self.kwargs['journey_id'])

    def perform_create(self, serializer):
        journey = Journey.objects.get(id=self.kwargs['journey_id'])
        serializer.save(user=self.request.user, journey=journey)


class JourneyCommentsUpdateAndDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Return one journey by id

    put/patch:
    Update journey by id

    delete:
    Delete journey
    """
    permission_classes = (IsOwner,)
    serializer_class = JourneyCommentsSerializer
    queryset = Comment.objects.all()
    lookup_field = 'id'


# ORDER API----------------------------------------------------------------------------------------------------
class OrderAnonimAPIView(generics.CreateAPIView):
    """
    create:
    Create new OrderAnonim
    """
    serializer_class = OrderAnonimSerializer
    queryset = OrderAnonim.objects.all()


class OrderAPIView(generics.CreateAPIView):
    """
    create:
    Create new order for journey
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = 'journey_id'

    def perform_create(self, serializer):
        journey = Journey.objects.get(id=self.kwargs['journey_id'])
        user = self.request.user
        email_address = self.request.user.email
        status = 0
        persons = int(self.request.data.get('persons', 1))
        if journey.sale_price:
            total = int(journey.sale_price * persons)
        else:
            total = int(journey.price * persons)
        serializer.save(user=user, journey=journey, email_address=email_address, status=status, total=total)
