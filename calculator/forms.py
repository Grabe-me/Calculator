from django import forms
from .models import FirstPage

class OperationForm(forms.ModelForm):
    text = forms.CharField(max_length=20)
    class Meta:
        model = FirstPage
        fields = ['text']
        labels = {'text': ''}

    def get_operation(self):
        operation = self.cleaned_data['text']
        return operation