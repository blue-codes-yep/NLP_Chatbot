from django.shortcuts import redirect, render
from django.shortcuts import HttpResponse


def home(request):
    return render(request, 'home.html')
