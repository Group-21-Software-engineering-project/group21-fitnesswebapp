from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.

def foodTracker(request):
    return render(request, 'foodTracker/foodTrackerHome.html')

@login_required
def log(request, exercise_log_id = None):
    instance = food_tracker_tbl()
    if food_tracker_tbl:
        instance = get_object_or_404(food_tracker_tbl, pk=exercise_log_id)
    else:
        instance = food_tracker_tbl()

    form = foodForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        your_object = form.save(commit=False)
        your_object.user = request.user
        your_object.save()
        return redirect('calendar-page')
    return render(request, 'exercise/form.html', {'form':form})