from datetime import datetime as dt
from datetime import timedelta
from datetime import date
import datetime
import calendar
from django.shortcuts import render , redirect, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from .forms import ExerciseForm
from .models import *
from .utils import Calendar
# Create your views here.

def exercise(request):
    return render(request, 'exercise/exercise.html')

class CalendarView(generic.ListView):
    model = exerciseLog
    template_name = 'exercise/calender.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #formats calander based on month we select using buttons, default is current month
        d = get_date(self.request.GET.get('month', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)

        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context
        

#button to iterate to previous month
def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


#button to iterate to next month
def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

#returns todays month to start on the calendar page
def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

#view for the log a request
def log(request, exercise_log_id = None):
    instance = exerciseLog()
    if exercise_log_id:
        instance = get_object_or_404(exerciseLog, pk=exercise_log_id)
    else:
        instance = exerciseLog()

    form = ExerciseForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return redirect('calendar-page')
    return render(request, 'exercise/form.html', {'form':form})