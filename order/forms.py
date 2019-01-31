from django import forms
from order.models import OrderAnonim
from django.utils.translation import gettext_lazy as _


class CreateOrderAnonim(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label=_("Призвіще та ім'я"))
    duration = forms.IntegerField(label=_("Тривалість"))
    person = forms.IntegerField(label=_("Кількість осіб"))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}), label=_('Що б Ви хотіли побачити?'))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}), label=_("Email-адреса"))

    class Meta:
        model = OrderAnonim
        fields = ('name', 'person', 'duration', 'description', 'phone', 'email')
