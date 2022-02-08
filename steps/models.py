from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

import datetime


class DailySteps(models.Model):
    steps_input = models.IntegerField(
        validators=[
            MaxValueValidator(50000),
            MinValueValidator(1)
        ]
    )
    steps_date = models.DateField(
        unique=True,
        validators= [ 
            MaxValueValidator(datetime.date.today, 
            message="The date cannot be in the future")
        ]
    )
    def __str__(self):
        return str(self.steps_date)