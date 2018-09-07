from django import forms
from allauth.account.forms import SignupForm

from pages.models import Feedback


class FeedbackForm(forms.ModelForm):
    name = forms.CharField(label='Будь-ласка, додайте Ваше імя та прізвище')
    body_text = forms.CharField(label='Залиште відгук', widget=forms.Textarea())

    class Meta:
        model = Feedback
        fields = ('name', 'body_text')


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=40, label="Ім'я")

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.save()
        return user
