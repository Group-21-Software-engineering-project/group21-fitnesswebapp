from django.shortcuts import render
from .models import body_stats_tbl
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


def updateBodyStats(request):
    if request.method == "POST":
        if request.POST.get('bodyStatHeight') and request.POST.get('unitHeight') and request.POST.get(
                'bodyStatWeight') and request.POST.get('unitWeight'):
            updateStats = body_stats_tbl()
            updateStats.bodyStatHeight = request.POST.get('bodyStatHeight')
            updateStats.unitHeight = request.POST.get('unitHeight')
            updateStats.bodyStatWeight = request.POST.get('bodyStatWeight')
            updateStats.unitWeight = request.POST.get('unitHeight')
            updateStats.save()

            return render(request, 'bodyStats/templates/bodyStatsHome.html')
        else:
            return render(request, 'bodyStats/templates/bodyStatsHome.html')
