from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'home/index.html')

def profile(request):
    return render(request, 'home/profile.html')

def login(request):
    return render(request, 'home/loginSignUp.html')