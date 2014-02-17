__author__ = 'archen'

# Core Python imports

# Core Django imports
from django.forms import ModelForm

# Third party imports
from datetimewidget.widgets import DateTimeWidget

# App-specific imports
from feeders.models import Feeder, Feeding, Hatch, Batch


class FeederForm(ModelForm):

    class Meta:
        model = Feeder
        fields = ('short_name', 'long_name', 'gallery')


class FeedingForm(ModelForm):
    class Meta:
        model = Feeding
        fields = ('feeder', 'accepted', 'total_fed', 'feeding_date')


class HatchForm(ModelForm):
    class Meta:
        model = Hatch
        fields = ('date', 'hatched_from', 'num_hatched')
        widgets = {
            'date': DateTimeWidget(),
        }


class BatchForm(ModelForm):
    class Meta:
        model = Batch
        fields = ('name', 'container', 'date_received', 'num_pupae', 'num_larvae', 'num_died', 'feeder')
        widgets = {
            'date_received': DateTimeWidget(),
        }