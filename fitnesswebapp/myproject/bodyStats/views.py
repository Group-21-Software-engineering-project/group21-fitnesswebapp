from django.shortcuts import render
from . import models
from .models import body_stats_tbl
from django.shortcuts import render, redirect
from .forms import bodyStatsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here
def bodyStatsUpdate(request):
    return render(request, 'bodyStats/bodyStatsUpdate.html')


def bodyStatsView(request):
    return render(request, 'bodyStats/bodyStatsView.html')


@login_required
def update_stats(request):
    form = bodyStatsForm(request.POST)
    instance = bodyStatsForm()
    if request.method == 'POST':
        if request.POST and form.is_valid():
            your_object = form.save(commit=False)
            your_object.user = request.user
            your_object.save()
            form = bodyStatsForm(request.POST or None, instance=instance)
            form.save()
            # process data here
            # userID = request.user
            # print(userID.id)
            messages.success(request, f'Body stats have been updated')
            return redirect('bodyStatsUpload-page')
    return render(request, 'bodyStats/bodyStatsUpload.html', {'form': form})


@login_required
def get_stats(request):
    redirect('bodyStatsView-page')
    query_result = body_stats_tbl.objects.all()
    return render(request, 'bodyStats/bodyStatsView.html', locals())



