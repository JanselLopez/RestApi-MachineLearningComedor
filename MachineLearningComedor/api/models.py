from calendar import week
from tkinter import CASCADE
from django.db import models

# Create your models here..
class InfoFood(models.Model):
    week_day = models.IntegerField()
    total_food_value = models.FloatField()
    people_percentage = models.FloatField()

