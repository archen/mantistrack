__author__ = 'archen'

# Core Python imports
from datetime import datetime

# Core Django imports
from django.db import models
from django.forms import fields, ModelForm
from django.contrib.contenttypes.generic import generic_inlineformset_factory

# Third party imports
from datetimewidget.widgets import DateTimeWidget

# App-specific imports
from notes.models import Note


class NoteForm(ModelForm):
    date = fields.DateTimeField(initial=datetime.now())

    class Meta:
        model = Note
        fields = ('date', 'is_public', 'content')
        widgets = {
            'date': DateTimeWidget(),
        }


def formfield_callback(field):
    if isinstance(field, models.DateTimeField) and field.name == 'date':
        return fields.DateTimeField(widget=DateTimeWidget, initial=datetime.now())
    return field.formfield()


NoteFormSet = generic_inlineformset_factory(Note, extra=1, formfield_callback=formfield_callback)