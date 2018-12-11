from django.db import models
from django.utils import timezone


# Create your models here.
class Student(models.Model):
    name = models.TextField()
    is_signedin = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    @staticmethod
    def submitted(name):
        Student(name=name).save()
