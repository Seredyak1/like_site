from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db.models import F
from django.utils.translation import gettext_lazy as _, get_language


class CampManager(models.Manager):

    def get_queryset(self):
        locale = get_language()
        return super().get_queryset().annotate(title=F('title_' + locale),
                                               description=F('description_' + locale),
                                               seo_title=F('seo_title_' + locale),
                                               short_description=F('short_description_' + locale))


class Camp(models.Model):
    class Meta:
        verbose_name = "Табір"
        verbose_name_plural = "Табори"
        ordering = ('updated_at',)


    title_uk = models.TextField(max_length=255, verbose_name=_('Назва табору Українською'))
    title_en = models.TextField(max_length=255, verbose_name=_('Назва табору Англійською'))
    seo_title_uk = models.CharField(max_length=255, verbose_name=_('SEO title'), blank=True,
                                    help_text='Заголовок для пошукового бота українською')
    seo_title_en = models.CharField(max_length=255, verbose_name=_('SEO title'), blank=True,
                                    help_text='Заголовок для пошукового бота англійською')
    short_description_uk = RichTextField(verbose_name=_('Короткий опис табору українською'))
    short_description_en = RichTextField(verbose_name=_('Короткий опис англійською'), blank=True)
    description_uk = RichTextField(verbose_name=_('Опис табору українською'))
    description_en = RichTextField(verbose_name=_('Опис табору англійською'), blank=True)
    price = models.IntegerField(verbose_name=_('Ціна у грн'))
    sale_price = models.IntegerField(verbose_name=_('Ціна зі скидкою у грн'), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата створення'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Дата останнього оновлення'))
    slug = models.SlugField(unique=True, default='', verbose_name=_('Назва табору в URL'))

    object = CampManager()

    def __str__(self):
        return self.title_uk

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('journey_details', args=[str(self.id)])


class CampPhoto(models.Model):

    camp = models.ForeignKey(Camp, related_name='camp_photos', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='camp-photos')


class CampDates(models.Model):

    camp = models.ForeignKey(Camp, related_name='dates', on_delete=models.CASCADE)
    start_date = models.DateField(verbose_name=_('початок табору'), blank=False, null=False)
    end_date = models.DateField(verbose_name=_('кінець табору'), blank=False, null=False)


class CampComment(models.Model):
    class Meta:
        ordering = ('-created_at',)

    camp = models.ForeignKey(Camp, related_name='comments_camp', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments_camp', on_delete=False)
    body = models.TextField(verbose_name=_('Відгук про табір'))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body


