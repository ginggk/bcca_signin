from django.forms import Form
from django import forms


class SignInForm(Form):
    name = forms.CharField(label='Name')


class CheckForm(Form):
    date = forms.DateField(input_formats=["%Y/%m/%d"], label='Date\nYY/MM/DD')
