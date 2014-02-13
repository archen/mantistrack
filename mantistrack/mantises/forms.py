__author__ = 'archen'

from django import forms
from datetimewidget.widgets import DateTimeWidget

from mantises.models import Mantis, Breed, Molt


class MantisForm(forms.ModelForm):
    class Meta:
        model = Mantis
        fields = ('name', 'breed', 'born', 'died', 'sex', 'notes', 'gallery')
        widgets = {
            'born': DateTimeWidget(),
            'died': DateTimeWidget(),
        }


class BreedForm(forms.ModelForm):
    class Meta:
        model = Breed
        fields = ('picture', 'short_name', 'long_name', 'life_expectancy',
                  'low_temperature', 'high_temperature', 'low_humidity', 'high_humidity')


class MoltForm(forms.ModelForm):
    class Meta:
        model = Molt
        fields = ('date', 'from_instar', 'to_instar')
        widgets = {
            'date': DateTimeWidget(),
        }