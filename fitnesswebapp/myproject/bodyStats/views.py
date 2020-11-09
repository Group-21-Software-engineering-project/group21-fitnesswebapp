from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def bodyStats(request):
    return render(request, 'bodyStats/bodyStatsHome.html')


def bodyStatsHistoryBMI(request):
    return render(request, 'bodyStats/bodyStatsHistoryBMI.html')


def bodyStatsHistoryHeight(request):
    return render(request, 'bodyStats/bodyStatsHistoryHeight.html')


def bodyStatsHistoryWeight(request):
    return render(request, 'bodyStats/bodyStatsHistoryWeight.html')
