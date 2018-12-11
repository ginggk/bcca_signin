from django.shortcuts import render, redirect
from django.views import View
from . import forms
from signins import models
from datetime import date

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
            today = date.today()
            if name in student_list:
                recent = len(models.Student.objects.filter(name=name))
                if today != models.Student.objects.filter(
                        name=name)[recent - 1].is_signedin:
                    models.Student.submitted(name)
                    return redirect('home')
                else:
                    return render(request, 'signin.html', {'form': form})
            else:
                return render(request, 'signin.html', {'form': form})
        else:
            return render(request, 'signin.html', {'form': form})


class Check(View):
    def get(self, request):
        return render(request, 'signin_check.html',
                      {'form': forms.CheckForm()})

    def post(self, request):
        form = forms.CheckForm(data=request.POST)
        # date_requested = Chec
        if form.is_valid():
            date = form.cleaned_data['date']
            students = models.Student.attendance(date)
            return render(request, 'signin_check.html', {
                'form': form,
                'students': students
            })
        else:
            return render(request, 'signin_check.html', {'form': form})
