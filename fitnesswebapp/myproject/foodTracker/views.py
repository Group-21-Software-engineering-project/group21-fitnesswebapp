from django.shortcuts import render


# Create your views here.

def foodTracker(request):
    return render(request, 'foodTracker/foodTrackerHome.html')
