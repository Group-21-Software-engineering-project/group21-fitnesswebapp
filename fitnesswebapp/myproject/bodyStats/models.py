from django.core.validators import MinValueValidator
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.

# Specifying the body_stats_tbl table for the database so users can store their body stats


class body_stats_tbl(models.Model):
    bs_entry_id = models.AutoField('body stat entry id', primary_key=True, unique=True, db_index=True, null=False)
    bs_date = models.DateTimeField('Date Recorded', default=datetime.now)
    height = models.DecimalField('Height cm', max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])
    weight = models.DecimalField('Weight kg', max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])
    bmi = models.DecimalField('BMI', max_digits=4, decimal_places=2, validators=[MinValueValidator(0)])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
