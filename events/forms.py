from django import forms
from django.forms import ModelForm

from .models import EventLocation


class EventLocationForm(ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget, label='Дата')
    time = forms.TimeField(widget=forms.TimeInput, label='Время')

    class Meta:
        model = EventLocation
        fields = '__all__'
