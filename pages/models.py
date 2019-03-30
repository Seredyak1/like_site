from django.db import models
from ckeditor.fields import RichTextField
from django.db.models import F
from django.utils.translation import gettext_lazy as _, get_language


class ClientCompany(models.Model):
    class Meta:
        verbose_name = "Клієнт-Компанія"
        verbose_name_plural = "Клієнт-Компанії"

    title = models.CharField(max_length=255, verbose_name='Назва компанії', blank=True)
    logo = models.ImageField(upload_to='companies-logo', verbose_name='Лого')
    site = models.CharField(max_length=255, verbose_name='Сайт', blank=True)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    class Meta:
        verbose_name = _("Відгук")
        verbose_name_plural = _("Відгуки")
        ordering = ("-created_at",)

    name = models.CharField(max_length=255, verbose_name=_('Імя'), blank=True)
    body_text = models.TextField(verbose_name=_('Відгук'))
    created_at = models.DateField(auto_now_add=True)
    is_published = models.BooleanField(default=False, verbose_name='Опубліковано?')

    def __str__(self):
        return self.name


class Document(models.Model):
    class Meta:
        verbose_name = "Документ"
        ordering = ('title_ukr',)

    title_ukr = models.CharField(max_length=255, verbose_name="Назва документу", blank=False, help_text="Назва українською")
    title_doc = models.CharField(max_length=255, verbose_name="Назва документу", blank=False, help_text="Назва англійською для скачування")
    document = models.FileField(upload_to='documentation')

    def __str__(self):
        return self.title_ukr


class FaqManager(models.Manager):

    def get_queryset(self):
        locale = get_language()
        return super().get_queryset().annotate(question=F('question_' + locale), answer=F('answer_' + locale))


class Faq(models.Model):
    class Meta:
        verbose_name = _("Типове запитання")
        verbose_name_plural = "Типові запитання"

    question_uk = RichTextField(blank=False, verbose_name=_("Типове Запитання українською"))
    answer_uk = RichTextField(blank=False, verbose_name=_("Відповідь українською"), null=True)
    question_en = RichTextField(blank=True, verbose_name=_("Типове Запитання англійською"))
    answer_en = RichTextField(blank=True, verbose_name=_("Відповідь англійською"), null=True)

    objects = FaqManager()

    def __str__(self):
        return self.question_uk
