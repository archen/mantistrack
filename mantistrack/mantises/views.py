from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.utils import IntegrityError
from django.views.generic.edit import CreateView, UpdateView

from datetime import datetime

# from photologue.models import Gallery

from mantises.models import Mantis, Molt, Breed, Ooth
from mantises.forms import MantisForm, BreedForm, MoltForm, OothForm


class MantisCreate(CreateView):
    model = Mantis
    form_class = MantisForm

    def get_form(self, form_class):
        form = super(MantisCreate, self).get_form(form_class)
        form.instance.user_id = self.request.user.id
        return form
"""
    Need to fix formatting of return for valid mantis creation

    def form_valid(self, form):
        gallery = Gallery(title=form.instance.name, title_slug=form.instance.name)
        gallery.save()
        form.instance.gallery = gallery
        return render(self.request, 'mantises/my_mantises.html')

"""


class MantisUpdate(UpdateView):
    model = Mantis
    form_class = MantisForm


class BreedCreate(CreateView):
    model = Breed
    form_class = BreedForm

    def get_form(self, form_class):
        form = super(BreedCreate, self).get_form(form_class)
        form.instance.user_id = self.request.user.id
        return form


class BreedUpdate(UpdateView):
    model = Breed
    form_class = BreedForm


class MoltCreate(CreateView):
    model = Molt
    form_class = MoltForm

    def get_form(self, form_class):
        form = super(MoltCreate, self).get_form(form_class)
        form.instance.user_id = self.request.user.id
        form.instance.mantis_id = self.kwargs['mantis_id']

        return form


class MoltUpdate(UpdateView):
    model = Molt
    form_class = MoltForm


class OothCreate(CreateView):
    model = Ooth
    form_class = OothForm

    def get_form(self, form_class):
        form = super(OothCreate, self).get_form(form_class)
        form.instance.user_id = self.request.user.id
        form.instance.mantis_id = self.kwargs['mantis_id']

        return form


class OothUpdate(UpdateView):
    model = Ooth
    form_class = OothForm


def index(request):
    # todo: change to most viewed
    top_mantis_list = Mantis.objects.order_by('-name')[:5]
    # todo: change to most mantises in breed
    top_breed_list = Breed.objects.order_by('-short_name')[:5]
    context = {
        'top_mantis_list': top_mantis_list,
        'top_breed_list': top_breed_list,
    }
    return render(request, 'mantises/index.html', context)


def breeds(request):
    breed_list = Breed.objects.all()
    context = {'breed_list': breed_list}
    return render(request, 'mantises/breeds.html', context)


def detail_mantis(request, mantis_id):
    mantis = get_object_or_404(Mantis, pk=mantis_id)
    ooth_list = mantis.ooth_set.all()

    if ooth_list:
        context = {'mantis': mantis, 'ooth_list': ooth_list}
    else:
        context = {'mantis': mantis}

    return render(request, 'mantises/mantis_detail.html', context)


def detail_breed(request, breed_id):
    breed = get_object_or_404(Breed, pk=breed_id)
    return render(request, 'mantises/breed_detail.html', {'breed': breed})


@login_required
def my_mantises(request):
    mantis_list = Mantis.objects.filter(user_id=request.user.id)
    context = {'mantis_list': mantis_list}
    return render(request, 'mantises/my_mantises.html', context)


@login_required
def do_molt(request, mantis_id):
    mantis = get_object_or_404(Mantis, pk=mantis_id)

    try:
        molt_record = Molt(mantis_id=mantis.id, user_id=request.user.id, date=datetime.now(mantis.born.tzinfo),
                           from_instar=mantis.instar(), to_instar=mantis.instar()+1)
        molt_record.save()
    except IntegrityError:
        return render(request, 'mantises/mantis_detail.html', {
            'mantis': mantis,
            'error_message': 'Error saving molt record.',
        })

    return render(request, 'mantises/mantis_detail.html', {'mantis': mantis})


@login_required
def molt_history(request, mantis_id):
    mantis = get_object_or_404(Mantis, pk=mantis_id)
    history = Molt.objects.filter(mantis=mantis)

    return render(request, 'mantises/molt_history.html', {'history': history, 'mantis': mantis})


def my_ooths(request):
    ooth_list = Ooth.objects.filter(user_id=request.user.id)

    return render(request, 'mantises/my_ooths.html', {'ooth_list': ooth_list})


def ooth_detail(request, mantis_id, ooth_id):
    mantis = get_object_or_404(Mantis, pk=mantis_id)
    ooth = get_object_or_404(Ooth, pk=ooth_id)

    return render(request, 'mantises/ooth_detail.html', {'mantis': mantis, 'ooth': ooth})