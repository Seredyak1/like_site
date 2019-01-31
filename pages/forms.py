from django import forms
from allauth.account.forms import SignupForm
from django.utils.translation import gettext_lazy as _

from pages.models import Feedback


class FeedbackForm(forms.ModelForm):
    name = forms.CharField(label=_('Будь-ласка, додайте Ваше імя та прізвище'))
    body_text = forms.CharField(label=_('Залиште відгук'), widget=forms.Textarea())

    class Meta:
        model = Feedback
        fields = ('name', 'body_text')


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=40, label="Ім'я")

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.save()
        return user
