from django import forms
from .models import Question


class Question_form(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
