from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.

def foodTracker(request):
    return render(request, 'foodTracker/foodTrackerHome.html')
