from rest_framework import serializers
from django.utils.translation import gettext_lazy as _, get_language
from django.db.models import F

from news.models import *
from pages.models import *
from camp.models import *
from product.models import *
from order.models import *


# NEWS SERIALIZER---------------------------------------------------------------------------------------------
class NewsPreviewSerializer(serializers.ModelSerializer):
    """Serializer for News"""
    first_image = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ['title_uk', 'title_en', 'short_description_uk', 'short_description_uk', 'first_image']

    def get_first_image(self, instance):
        try:
            first_image = NewsPhoto.objects.filter(news=instance.id).first().image.url
        except:
            first_image = None
        return first_image


class NewsSerializer(serializers.ModelSerializer):

    images = serializers.SerializerMethodField()

    class Meta:
        model = NewsPhoto
        fields = '__all__'

    def get_images(self, instance):
        images = []
        try:
            image = NewsPhoto.objects.filter(news=instance.id)
            for el in image:
                images.append(el.image.url)
        except:
            pass
        return images


# PAGES API----------------------------------------------------------------------------------------------------
class ClientCompanySerializer(serializers.ModelSerializer):
    """Serializer for Client Company model"""
    class Meta:
        model = ClientCompany
        fields = '__all__'


class DocumentsSerializer(serializers.ModelSerializer):
    """Serializer for Client Company model"""
    class Meta:
        model = Document
        fields = '__all__'


class FAQSerializer(serializers.ModelSerializer):
    """Serializer for FAQs"""

    class Meta:
        model = Faq
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    """Serializer for Feedback"""
    class Meta:
        model = Feedback
        fields = '__all__'
        read_only_fields = ['created_at', 'is_published']


# CAMP API----------------------------------------------------------------------------------------------------
class CampDatesSerializer(serializers.ModelSerializer):
    """Serializer for Camp dates"""
    class Meta:
        model = CampDates
        fields = ('start_date', 'end_date',)


class CampPreviewSerializer(serializers.ModelSerializer):
    """Serializer for Camp"""
    first_image = serializers.SerializerMethodField()
    dates = serializers.SerializerMethodField()

    class Meta:
        model = Camp
        fields = ('title_uk', 'title_en', 'short_description_uk', 'short_description_en', 'price', 'sale_price',
                  'slug', 'first_image', 'dates')

    def get_first_image(self, instance):
        try:
            first_image = CampPhoto.objects.filter(camp=instance.id).first().image.url
        except:
            first_image = None
        return first_image

    def get_dates(self, instance):
        dates = CampDates.objects.filter(camp=instance.id)
        serializer_for_dates = CampDatesSerializer(instance=dates, many=True)
        return serializer_for_dates.data


class CampDetailSerializer(serializers.ModelSerializer):
    """Serializer for Camp"""
    images = serializers.SerializerMethodField()
    dates = serializers.SerializerMethodField()

    class Meta:
        model = Camp
        fields = ('title_uk', 'title_en', 'seo_title_uk', 'seo_title_en', 'description_uk', 'description_en',
                  'price', 'sale_price', 'slug', 'images', 'dates')

    def get_images(self, instance):
        images = []
        try:
            image = CampPhoto.objects.filter(camp=instance.id)
            for el in image:
                images.append(el.image.url)
        except:
            pass
        return images

    def get_dates(self, instance):
        dates = CampDates.objects.filter(camp=instance.id)
        serializer_for_dates = CampDatesSerializer(instance=dates, many=True)
        return serializer_for_dates.data


class CampCommentSerializer(serializers.ModelSerializer):
    """Serializer for Camp comments"""
    class Meta:
        model = CampComment
        fields = '__all__'
        read_only_fields = ('user', 'created_at', 'is_published', 'camp')


# PRODUCT API----------------------------------------------------------------------------------------------------
class CategoryListSerializer(serializers.ModelSerializer):
    """Serializer for Categories
    Only title and slug field"""
    class Meta:
        model = Category
        fields = ('name_uk', 'name_en', 'slug',)


class CategoryDetailSerializer(serializers.ModelSerializer):
    """Serializer for Category detail"""
    class Meta:
        model = Category
        fields = '__all__'


class JourneyCardSerializer(serializers.ModelSerializer):
    """Serializer for Journey. Use for journey card"""
    first_image = serializers.SerializerMethodField()

    class Meta:
        model = Journey
        fields = ('sku', 'title_uk', 'title_en', 'price', 'sale_price', 'durations_days', 'durations_night',
                  'first_image',)

    def get_first_image(self, instance):
        try:
            image = JourneyPhoto.objects.filter(journey=instance.id).first().image.url
        except:
            image = None
        return image


class JourneySerializer(serializers.ModelSerializer):
    """Serializer for Journey. Use for full journey detail"""
    images = serializers.SerializerMethodField()

    class Meta:
        model = Journey
        fields = '__all__'

    def get_images(self, instance):
        images = []
        try:
            image = JourneyPhoto.objects.filter(journey=instance.id)
            for el in image:
                images.append(el.image.url)
        except:
            pass
        return images


class JourneyCommentsSerializer(serializers.ModelSerializer):
    """Serializer for JourneyComments"""

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'created_at', 'is_published', 'journey')


# ORDER API----------------------------------------------------------------------------------------------------
class OrderAnonimSerializer(serializers.ModelSerializer):
    """Serializer for OrderAnonim"""

    class Meta:
        model = OrderAnonim
        exclude = ('contacted',)


class OrderSerializer(serializers.ModelSerializer):
    """Serializer for Order"""

    class Meta:
        model = Order
        fields = ('contact_phone', 'persons',)
        read_only_field = ('email_address',)

    def create(self, validated_data):
        return Order.objects.create(**validated_data)