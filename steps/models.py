from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class DailySteps(models.Model):
    steps_input = models.IntegerField(
        validators=[
            MaxValueValidator(50000),
            MinValueValidator(1)
        ]
    )
    steps_date = models.DateField()
    def __str__(self):
        return str(self.steps_date)