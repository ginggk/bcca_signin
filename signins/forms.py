from django.forms import Form
from django import forms


class SignInForm(Form):
    name = forms.CharField(label='Name')


class CheckForm(Form):
    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        }))
