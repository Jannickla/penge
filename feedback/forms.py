from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('subject',
                  'feedback_description',
                  'overall_satisfaction')
        widgets = {'subject': forms.TextInput(attrs={'class': 'form-control'}),
                   'feedback_description': forms.TextInput(attrs={'rows': 10, 'cols': 20, 'class': 'form-control'})}
