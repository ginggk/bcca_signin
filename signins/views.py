from django.shortcuts import render, redirect
from django.views import View
from . import forms
from signins import models

# Create your views here.
student_list = [
    'Matthew Lipsey', 'Ginger Keys', 'Daniel Peterson', 'Cole Anderson',
    'John Morgan', 'Henry Moore', 'Ray Turner', 'Timothy Bowling',
    'Logan Harrell', 'Myeisha Madkins', 'Cody van der Poel'
]


class Home(View):
    def get(self, request):
        return render(request, 'home.html',
                      {'Students': models.Student.objects.all()})


class SignIn(View):
    def get(self, request):
        return render(request, 'signin.html', {'form': forms.SignInForm()})

    def post(self, request):
        form = forms.SignInForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            if name in student_list:
                models.Student.submitted(name)
                return redirect('home')
            else:
                return render(request, 'signin.html', {'form': form})
        else:
            return render(request, 'signin.html', {'form': form})
