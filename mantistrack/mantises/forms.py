__author__ = 'archen'

from django import forms
from datetimewidget.widgets import DateTimeWidget

from mantises.models import Mantis


class MantisForm(forms.ModelForm):
    class Meta:
        model = Mantis
        fields = ('name', 'breed', 'born', 'died', 'sex', 'notes', 'gallery')
        widgets = {
            'born': DateTimeWidget(),
            'died': DateTimeWidget(),
        }