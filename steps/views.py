from re import template
from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader


from .models import DailySteps
from .forms import DailyStepsForm


def index(request):
    # return render(request, 'steps/index.html')
  if request.method == "POST":
    form = DailyStepsForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = DailyStepsForm()
  return render(request, 'steps/index.html', {'form': form})

# class index(CreateView):
#     model = DailySteps
#     form_class = DailyStepsForm


def history(request):
    latest_dailysteps_list = DailySteps.objects.order_by('-steps_date')
    context = {'latest_dailysteps_list': latest_dailysteps_list}
    return render(request, 'steps/history.html', context)




    # response = "You're looking at the results of day %s."
    # return HttpResponse(response % dailysteps_id)