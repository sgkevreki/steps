from re import template
from django.shortcuts import redirect, render

from .models import DailySteps
from .forms import DailyStepsForm, DateFieldForm

from datetime import timedelta
from operator import attrgetter



def index(request):

  # Add steps form
  if request.method == "POST" and 'add_steps_btn' in request.POST:
    form_steps = DailyStepsForm(request.POST)
    if form_steps.is_valid():
      form_steps.save()
      return redirect('index')
  else:
    form_steps = DailyStepsForm()

  # Date range form
  if request.method == "POST" and 'date_range_btn' in request.POST:
    form_date_range = DateFieldForm(request.POST)
    if form_date_range.is_valid():
      cd = form_date_range.cleaned_data
      start_date = cd.get('start_date')
      end_date = cd.get('end_date')

      delta = end_date - start_date 

      steps_all_dates = DailySteps.objects.values_list('steps_date', flat=True)
      not_found_dates = []

      #creating a new list that contains all the dates/steps that are not in the database between start date and end date
      for i in range(delta.days + 1):
        new_date = start_date + timedelta(days=i)
        if new_date not in steps_all_dates:
          not_found_dates.append({'steps_input': 0, 'steps_date': new_date}) # 0 value to steps that the user haven't submitted 
        
      steps_all = DailySteps.objects.filter(steps_date__range=[start_date, end_date]).values('steps_input', 'steps_date')
      #adding the new list
      steps_all = list(steps_all)
      steps_all.extend(not_found_dates)
      steps_all.sort(key=lambda item:item['steps_date'])

  else:
    steps_all = []
    form_date_range = DateFieldForm()
   
  return render(request, 'steps/index.html', {'form_steps': form_steps, 'form_date_range': form_date_range, 'steps_all': steps_all,},  )