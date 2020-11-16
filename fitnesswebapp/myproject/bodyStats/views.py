from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from .forms import bodyStatsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.

def bodyStats(request):
    return render(request, 'bodyStats/bodyStatsHome.html')


# @login_required
# def updateBodyStats(request, bs_entry_id=None):
#  instance = body_stats_tbl()
# if bs_entry_id:
#    instance = get_object_or_404(body_stats_tbl, pk=bs_entry_id)
# else:
#  instance = body_stats_tbl()

# form = bodyStatsForm(request.POST or None, instance=instance)
# if request.POST and form.is_valid():
#  your_object = form.save(commit=False)
# your_object.user = request.user
# your_object.save()
# messages.success(request, f'body stats successfully updated')
# return redirect('bodyStats-page')
# return render(request, 'bodyStats/bodyStatsHome.html', {'form': form})


def updateStats(request):
    if request.method == 'POST':
        form = bodyStatsForm(request.POST)
        if form.is_valid():
            # process data here
            form.save()
            messages.success(request, f'Body stats have been updated')
            redirect('bodyStats-page')
    return render(request, 'bodyStats/bodyStatsHome.html', {'form': form})


# if request.POST.get('bodyStatHeight') and request.POST.get(
#      'bodyStatWeight') and request.POST.get('bodyStatDate') :
#    updateStats = body_stats_tbl()
#    updateStats.bodyStatHeight = request.POST.get('bodyStatHeight')
#    updateStats.bodyStatWeight = request.POST.get('bodyStatWeight')
#    updateStats.save()

#    return render(request, 'bodyStats/templates/bodyStatsHome.html')
# else:
#    return render(request, 'bodyStats/templates/bodyStatsHome.html')
