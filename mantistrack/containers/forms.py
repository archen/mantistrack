__author__ = 'archen'

# Core Django imports
from django import forms

# Third party imports
from datetimewidget.widgets import DateTimeWidget

# App-specific imports
from containers.models import Container, ContainerType, EnvironmentReading


class ContainerForm(forms.ModelForm):
    class Meta:
        model = Container
        fields = ('name', 'type')


class ContainerTypeForm(forms.ModelForm):
    class Meta:
        model = ContainerType
        fields = ('name', 'height', 'length', 'width', 'type', 'url')


class EnvironmentReadingForm(forms.ModelForm):
    class Meta:
        model = EnvironmentReading
        fields = ('date', 'temperature', 'humidity')
        widgets = {
            'date': DateTimeWidget(),
        }