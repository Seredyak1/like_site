from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db.models import F
from django.utils.translation import gettext_lazy as _, get_language


class CategoryManager(models.Manager):

    def get_queryset(self):
        locale = get_language()
        return super().get_queryset().annotate(name=F('name_' + locale), description=F('description_' + locale),
                                               seo_title=F('seo_title_' + locale))


class Category(models.Model):
    class Meta:
        verbose_name = _("Категорія")
        verbose_name_plural = _("Категорії")

    name_uk = models.CharField(max_length=255, verbose_name=_('Назва Категорії Українською'))
    name_en = models.CharField(max_length=255, verbose_name=_('Назва Категорії Англійською'), blank=True)
    seo_title_uk = models.CharField(max_length=255, verbose_name=_('SEO title укр'), blank=True,
                                    help_text='Заголовок для пошукового бота українською')
    seo_title_en = models.CharField(max_length=255, verbose_name=_('SEO title англ'), blank=True,
                                    help_text='Заголовок для пошукового бота англійською')
    slug = models.SlugField(unique=True, default='', verbose_name=_('Назва в URL'))
    description_uk = RichTextField(verbose_name=_('Опис Категорії'), blank=True)
    description_en = RichTextField(verbose_name=_('Опис Англійською'))
    category_logo = models.ImageField(upload_to='category-logo', null=True, verbose_name=_('Лого Категорії'))

    objects = CategoryManager()

    def __str__(self):
        return self.name_uk

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('category_detail', args=[self.slug])


class JourneyManager(models.Manager):

    def get_queryset(self):
        locale = get_language()
        return super().get_queryset().annotate(title=F('title_' + locale), description=F('description_' + locale),
                                               seo_title=F('seo_title_' + locale))


class Journey(models.Model):
    class Meta:
        verbose_name = _("Пригода")
        verbose_name_plural = _("Пригоди")
        ordering = ('-updated_at',)

    sku = models.CharField(max_length=255, verbose_name=_('Номер'))
    title_uk = models.CharField(max_length=255, verbose_name=_('Назва пригоди українською'))
    title_en = models.CharField(max_length=255, verbose_name=_('Назва пригоди англійською'), blank=True)
    seo_title_uk = models.CharField(max_length=255, verbose_name=_('SEO title'), blank=True,
                                    help_text='Заголовок для пошукового бота українською')
    seo_title_en = models.CharField(max_length=255, verbose_name=_('SEO title'), blank=True,
                                    help_text='Заголовок для пошукового бота англійською')
    description_uk = RichTextField(verbose_name=_('Опис пригоди українською'))
    description_en = RichTextField(verbose_name=_('Опис пригоди англійською'), blank=True)
    durations_days = models.IntegerField(verbose_name=_('Тривалість днів'))
    durations_night = models.IntegerField(verbose_name=_('Тривалість ночей'))
    price = models.IntegerField(verbose_name=_('Ціна у грн'))
    sale_price = models.IntegerField(verbose_name=_('Ціна зі скидкою у грн'), null=True, blank=True)
    category = models.ForeignKey(Category, related_name='Journeys', on_delete=models.CASCADE, verbose_name=_('Категорія'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата створення'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Дата останнього оновлення'))

    objects = JourneyManager()

    def __str__(self):
        return self.title_uk

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('journey_details', args=[str(self.id)])


class JourneyPhoto(models.Model):
    journey = models.ForeignKey(Journey, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='journeys-photos')


class Comment(models.Model):
    class Meta:
        ordering = ('-created_at',)

    journey = models.ForeignKey(Journey, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=False)
    body = models.TextField(verbose_name=_('Відгук'))
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False, verbose_name=_("Опубліковано?"))

    def __str__(self):
        return self.body
