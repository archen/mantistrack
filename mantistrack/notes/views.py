# Core Python imports

# Core Django imports
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.contenttypes.models import ContentType

# App-specific imports
from notes.models import Note
from notes.forms import NoteForm


class NoteCreate(CreateView):
    model = Note
    form_class = NoteForm

    def get_form(self, form_class):
        print(self.success_url)
        form = super(NoteCreate, self).get_form(form_class)
        form.instance.user_id = self.request.user.id
        form.instance.content_type = get_object_or_404(ContentType, model=self.kwargs['content_type'])
        form.instance.object_id = self.kwargs['object_id']
        return form

    def get_success_url(self):
        form = super(NoteCreate, self).get_form(self.form_class)
        model = form.save(commit=False)
        return model.content_object.get_absolute_url()


class NoteUpdate(UpdateView):
    model = Note
    form_class = NoteForm

    def get_success_url(self):
        form = super(NoteUpdate, self).get_form(self.form_class)
        model = form.save(commit=False)
        return model.content_object.get_absolute_url()