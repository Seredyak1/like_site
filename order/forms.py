from django import forms
from order.models import Order, OrderAnonim


class CreateOrder(forms.ModelForm):
    contact_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Номер телефону")
    persons = forms.IntegerField(label="Кількість осіб")

    class Meta:
        model = Order
        fields = ('contact_phone', 'persons',)


class CreateOrderAnonim(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Призвіще та ім'я")
    duration = forms.IntegerField(label="Тривалість")
    person = forms.IntegerField(label="Кількість осіб")
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}), label='Що б Ви хотіли побачити?')
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Email-адреса")

    class Meta:
        model = OrderAnonim
        fields = ('name', 'person', 'duration', 'description', 'phone', 'email')
