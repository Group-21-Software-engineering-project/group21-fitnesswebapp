from django.shortcuts import render
from .models import body_stats_tbl
from django.shortcuts import render, redirect, get_object_or_404
from .forms import bodyStatsForm
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.

def bodyStats(request):
    return render(request, 'bodyStats/bodyStatsHome.html')


def updateBodyStats(request):
    if request.method == "POST":
        form = bodyStatsForm(request.POST)
        if form.is_valid():
            # process data here
            messages.success(request, f'body stats have been updated')
            return redirect('bodyStats-page')

        #if request.POST.get('bodyStatHeight') and request.POST.get('unitHeight') and request.POST.get(
        #      'bodyStatWeight') and request.POST.get('unitWeight'):
        #    updateStats = body_stats_tbl()
        #    updateStats.bodyStatHeight = request.POST.get('bodyStatHeight')
        #    updateStats.unitHeight = request.POST.get('unitHeight')
        #    updateStats.bodyStatWeight = request.POST.get('bodyStatWeight')
        #    updateStats.unitWeight = request.POST.get('unitHeight')
        #    updateStats.save()

        #    return render(request, 'bodyStats/templates/bodyStatsHome.html')
        #else:
        #    return render(request, 'bodyStats/templates/bodyStatsHome.html')
