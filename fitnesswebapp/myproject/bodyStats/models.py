from django.db import models
from django.conf import settings


# Create your models here.

# Specifying the body_stats_tbl table for the database
class body_stats_tbl(models.Model):
    bs_entry_id = models.AutoField('body stat entry id', primary_key=True, unique=True, db_index=True, null=False)
    bs_date = models.DateTimeField('Body stat date', null=False)
    height = models.DecimalField('body height', null=False, max_digits=5, decimal_places=2)
    weight = models.DecimalField('body weight', null=False, max_digits=5, decimal_places=2)
    bmi = models.DecimalField('body bmi', null=False, max_digits=4, decimal_places=2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
