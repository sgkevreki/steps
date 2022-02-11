from re import template
from django.shortcuts import redirect, render

from django.http import HttpResponse
from django.template import loader

from django.http import JsonResponse

from .models import DailySteps
from .forms import DailyStepsForm, DateFieldForm


def index(request):
  if request.method == "POST" and 'submit1' in request.POST:
    form_steps = DailyStepsForm(request.POST)
    if form_steps.is_valid():
      form_steps.save()
      return redirect('index')
  else:
    form_steps = DailyStepsForm()

  if request.method == "POST" and 'submit2' in request.POST:
    form_date_range = DateFieldForm(request.POST)
    if form_date_range.is_valid():
      cd = form_date_range.cleaned_data
      start_date = cd.get('start_date')
      end_date = cd.get('end_date')
      steps_all = DailySteps.objects.order_by('steps_date').filter(steps_date__range=[start_date, end_date])
  else:
    steps_all = DailySteps.objects.order_by('steps_date')
    form_date_range = DateFieldForm()
   
  return render(request, 'steps/index.html', {'form_steps': form_steps, 'form_date_range': form_date_range, 'steps_all': steps_all},  )