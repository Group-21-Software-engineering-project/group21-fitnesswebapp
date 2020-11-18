from django.shortcuts import render, get_object_or_404
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


# allow user to upload their body stats to the database table
@login_required  # users have to be logged in to access the body stats upload page
def update_stats(request, update_stats_id=None):
    if update_stats_id:
        instance = get_object_or_404(bodyStatsForm, pk=update_stats_id)
    else:
        instance = body_stats_tbl()

    form = bodyStatsForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        your_object = form.save(commit=False)
        your_object.user = request.user
        your_object.save()
        messages.success(request, f'Body stats have been updated')
        return redirect('bodyStatsUpload-page')
    return render(request, 'bodyStats/bodyStatsUpload.html', {'form': form})


@login_required  # users have to be logged in to access the body stats view page
def get_stats(request):
    data = body_stats_tbl.objects.values_list('bs_date', 'height', 'weight', 'bmi', 'user')  # create a variable as an object made up of all of the attributes that are stated
    bodyStats = {  # turns the variable data which is a querySet to a dictionary
        'data': data
    }
    # for item in data:  used for testing what the server is getting from the database
    #   print(item)
    #   print(type(item))
    return render(request, 'bodyStats/bodyStatsView.html', bodyStats)
