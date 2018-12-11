from django.forms import Form
from django import forms


class SignInForm(Form):
    name = forms.CharField(label='Name')
