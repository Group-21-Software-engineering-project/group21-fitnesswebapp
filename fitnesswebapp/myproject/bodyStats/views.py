from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def bodyStats(request):
    return render(request, 'bodyStats/bodyStatsHome.html')
