from django import forms

from . models import todo_text

class texts(forms.ModelForm):
    class Meta:
        model = todo_text
        fields = ['text']