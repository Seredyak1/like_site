from django import forms
from order.models import Order


class CreateOrder(forms.Form):
    contact_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Order
        fields = ('contact_phone',)
