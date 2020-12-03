from django import forms


class TimezoneAlarmForm(forms.Form):
    name = forms.CharField(max_length=100)
    alarm = forms.DateTimeField(localize=True, widget=forms.DateTimeInput())