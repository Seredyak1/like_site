from django import forms
from django.utils.translation import gettext_lazy as _

from order.models import OrderAnonim, CampOrder
from camp.models import CampDates



class CreateOrderAnonim(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label=_("Призвіще та ім'я"))
    duration = forms.IntegerField(label=_("Тривалість"))
    person = forms.IntegerField(label=_("Кількість осіб"))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}), label=_('Що б Ви хотіли побачити?'))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}), label=_("Email-адреса"))

    class Meta:
        model = OrderAnonim
        fields = ('name', 'person', 'duration', 'description', 'phone', 'email')


class CreateCampOrder(forms.ModelForm):
    class Meta:
        model = CampOrder
        fields = ('name', 'age', 'city', 'dates', 'special', 'email', 'phone')

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label=_("Призвіще та ім'я"))
    age = forms.IntegerField(label=_("Вік"))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label=_("Місто"))
    dates = forms.ModelChoiceField(queryset=CampDates.objects.all(), label=_("Виберіть дати:"))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label=_("Номер телефону"))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}), label=_("Email-адреса"))
