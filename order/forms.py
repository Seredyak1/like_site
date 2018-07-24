from django import forms
from order.models import OrderAnonim


class CreateOrderAnonim(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Призвіще та ім'я")
    duration = forms.IntegerField(label="Тривалість")
    person = forms.IntegerField(label="Кількість осіб")
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}), label='Що б Ви хотіли побачити?')
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Email-адреса")

    class Meta:
        model = OrderAnonim
        fields = ('name', 'person', 'duration', 'description', 'phone', 'email')
