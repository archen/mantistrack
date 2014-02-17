__author__ = 'archen'

# Core Django imports
from django import forms

# Third party imports
from datetimewidget.widgets import DateTimeWidget

# App-specific imports
from mantises.models import Mantis, Breed, Molt, Ooth


class MantisForm(forms.ModelForm):
    class Meta:
        model = Mantis
        fields = ('name', 'breed', 'born', 'died', 'sex', 'gallery', 'container', 'from_colony')
        widgets = {
            'born': DateTimeWidget(),
            'died': DateTimeWidget(),
        }


class BreedForm(forms.ModelForm):
    class Meta:
        model = Breed
        fields = ('picture', 'short_name', 'long_name', 'life_expectancy', 'adult_instar_male', 'adult_instar_female',
                  'low_temperature', 'high_temperature', 'low_humidity', 'high_humidity')


class MoltForm(forms.ModelForm):
    class Meta:
        model = Molt
        fields = ('date', 'from_instar', 'to_instar')
        widgets = {
            'date': DateTimeWidget(),
        }


class OothForm(forms.ModelForm):
    class Meta:
        model = Ooth
        fields = ('name', 'picture', 'laid_by', 'date_laid', 'date_hatched', 'container', 'nymphs')
        widgets = {
            'date_laid': DateTimeWidget(),
            'date_hatched': DateTimeWidget(),
        }