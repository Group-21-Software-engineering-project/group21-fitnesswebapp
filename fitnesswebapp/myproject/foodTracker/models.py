from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.

class food_tracker_tbl(models.Model):
    food_id = models.AutoField('food item id', primary_key=True, unique=True, db_index=True, null=False)
    food_date = models.DateTimeField('food item date', null=False)
    food_name = models.TextField('food item name', null=False, max_length="200")
    food_weight = models.PositiveIntegerField('food weight', null=False, validators=[MinValueValidator(1)])
    food_calories = models.PositiveIntegerField('food calories', null=False, validators=[MinValueValidator(1)])
    food_carbohydrates = models.PositiveIntegerField('food carbohydrates', null=False, validators=[MinValueValidator(1)])
    food_protein = models.PositiveIntegerField('food protein', null=False, validators=[MinValueValidator(1)])
    food_fat = models.PositiveIntegerField('food fat', null=False, validators=[MinValueValidator(1)])
