from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

exercise_type_choices = (
    ('cardio','Cardio'),
    ('bench press','Bench Press'),
    ('sit ups','Sit Ups'),
    ('biceps','Biceps'),
    ('other','Other'),
)

#exercise log model.
class exerciseLog(models.Model):
    day = models.DateTimeField(default=datetime.now, blank=True)
    hours = models.FloatField()
    minutes = models.FloatField()
    exercise_type = models.CharField(max_length=100, choices=exercise_type_choices, default='Cardio')
    notes = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    #this is so each entry can be edited
    @property
    def get_html_url(self):
        url = reverse('form-edit-page', args=(self.id,))
        return f'<a href="{url}"> {self.exercise_type} </a>'