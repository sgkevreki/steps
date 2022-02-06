from turtle import width
from django import forms
from django.forms import ModelForm

from .models import DailySteps
 

class DateInput(forms.DateInput):
    input_type = 'date'

class DailyStepsForm(ModelForm):
  class Meta:
    model = DailySteps
    fields = ['steps_input', 'steps_date',]
    labels = {'steps_input': "Steps", 'steps_date': "Date",}
    widgets = {
        'steps_date': DateInput(),
    }