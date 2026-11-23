from django import forms
from .models import SurveyResponse


class SurveyResponseForm(forms.ModelForm):

    class Meta:
        model = SurveyResponse

        fields = [
            'name',
            'email',
            'technology',
            'rating',
            'feedback',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),

            'technology': forms.Select(attrs={
                'class': 'form-control'
            }),

            'rating': forms.Select(attrs={
                'class': 'form-control'
            }),

            'feedback': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your feedback',
                'rows': 4
            }),
        }