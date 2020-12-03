import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import TimezoneAlarmForm
from .models import MyTime


def form_view(request):
    if request.method == 'POST':
        form = TimezoneAlarmForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            alarm = form.cleaned_data['alarm']
            MyTime.objects.create(name=name, alarm=alarm)
            return HttpResponseRedirect('ok')

    else:
        form = TimezoneAlarmForm()

    return render(request, 'locale_form.html', {'form': form})
