from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import exerciseLog
from django.contrib.auth.models import User
from .forms import ExerciseForm



#creates the calander
class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None, user=None):
        self.year = year
        self.month = month
        self.user = user
        super(Calendar,self).__init__()

    #formats the days into <td> will only render the current logged in users logs into each td
    def formatday(self, day, events):
        events_per_day = events.filter(day__day=day).filter(user__username=self.user)
        d=''
        for event in events_per_day:
            d+= f'<li> {event.get_html_url} </li>'
        if day !=0:
            return f"<td><span class = 'date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    #formats weeks into <tr>
    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr>{week}</tr>'
        
    #formats month as each table
    def formatmonth(self, withyear=True):
        events = exerciseLog.objects.filter(day__year=self.year, 
        day__month=self.month)
    
        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'

        return cal