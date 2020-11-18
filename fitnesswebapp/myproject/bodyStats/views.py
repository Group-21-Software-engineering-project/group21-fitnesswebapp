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


# allow user to upload their body stats
@login_required
def update_stats(request, update_stats_id=None):
    instance = body_stats_tbl()
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


@login_required
def get_stats(request):
    current_user = request.user.id
    # print("The user id is (with current user): " + str(current_user.id))
    print("The user currently logged in is: " + str(current_user))
    # data = body_stats_tbl.objects.values('bs_date', 'height', 'weight', 'bmi', 'user')
    data = body_stats_tbl.objects.values_list('bs_date', 'height', 'weight', 'bmi', 'user')
    # data = body_stats_tbl.objects.all()
    # for current_user in data:
        # data = data.filter(user_id=current_user)
    bodyStats = {
        'data': data
    }
    print(type(data))
    for item in data:
        # print(item)
        # print(type(item))
        if item[-1] == current_user:
            print(item)
            # print(type(item))
    return render(request, 'bodyStats/bodyStatsView.html', bodyStats)
