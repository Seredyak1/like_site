from django import forms
from camp.models import CampComment


class CampCommentForm(forms.ModelForm):

    class Meta:
        model = CampComment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }