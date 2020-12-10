from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

# Create your models here.


# Specifying the food_tbl table for the database so users can store the food they have eaten


class food_tbl(models.Model):
    food_entry_id = models.AutoField('food entry id', default=datetime.now, primary_key=True, unique=True, db_index=True, null=False)
    food_date = models.DateTimeField('date recorded', default=datetime.now)
    food_name = models.TextField('food name')
    food_calories = models.IntegerField('food calories', validators=[MinValueValidator(1), MaxValueValidator(3000)])
    food_weight = models.IntegerField('food weight', validators=[MinValueValidator(1), MaxValueValidator(3000)])
    food_fat = models.IntegerField('food fat', validators=[MinValueValidator(1), MaxValueValidator(3000)])
    food_protein = models.IntegerField('food protein', validators=[MinValueValidator(1), MaxValueValidator(3000)])
    food_carbohydrates = models.IntegerField('food carbohydrates', validators=[MinValueValidator(1), MaxValueValidator(3000)])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
