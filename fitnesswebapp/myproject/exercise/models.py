from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse
from django.db import models
# Create your models here.

exercise_type_choices = (
    ('cardio','Cardio'),
    ('bench press','Bench Press'),
    ('sit ups','Sit Ups'),
    ('biceps','Biceps'),
)

#exercise log model.
class exerciseLog(models.Model):
    day = models.DateTimeField(default=datetime.now, blank=True)
    hours = models.FloatField()
    minutes = models.FloatField()
    exercise_type = models.CharField(max_length=100, choices=exercise_type_choices, default='Cardio')
    notes = models.TextField()