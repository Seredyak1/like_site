from django import forms

from pages.models import Feedback


class FeedbackForm(forms.ModelForm):
    name = forms.CharField(label='Будь-ласка, додайте Ваше імя та прізвище')
    body_text = forms.CharField(label='Залиште відгук', widget=forms.Textarea())

    class Meta:
        model = Feedback
        fields = ('name', 'body_text')
