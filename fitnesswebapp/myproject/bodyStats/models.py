from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.

# Specifying the body_stats_tbl table for the database so users can store their body stats
class body_stats_tbl(models.Model):
    bs_entry_id = models.AutoField('body stat entry id', primary_key=True, unique=True, db_index=True, null=False)
    bs_date = models.DateTimeField('Date Recorded')
    height = models.DecimalField('Height', max_digits=5, decimal_places=2)
    weight = models.DecimalField('Weight', max_digits=5, decimal_places=2)
    bmi = models.DecimalField('BMI', max_digits=4, decimal_places=2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
