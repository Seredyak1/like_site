from rest_framework import serializers

from news.models import News, NewsPhoto


#NEWS SERIALIZER
class NewsSerializer(serializers.ModelSerializer):
    """Serializer for News"""

    class Meta:
        model = News
        fields = '__all__'
        read_only_fields = ['created_at']


class NewsPhotoSerializer(serializers.ModelSerializer):

    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = NewsPhoto
        fields = '__all__'

    def get_image_url(self, obj):
        return obj.image.url
