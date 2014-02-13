from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.utils import IntegrityError
from django.views.generic.edit import CreateView, UpdateView

from datetime import datetime

# from photologue.models import Gallery

from mantises.models import Mantis, Molt, Breed
from mantises.forms import MantisForm, BreedForm


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
        return render(self.request, 'mantises/mymantises.html')

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


def index(request):
    top_mantis_list = Mantis.objects.order_by('-name')[:5]
    context = {'top_mantis_list': top_mantis_list}
    return render(request, 'mantises/index.html', context)


def breeds(request):
    breed_list = Breed.objects.all()
    context = {'breed_list': breed_list}
    return render(request, 'mantises/breeds.html', context)


def detail(request, mantis_id):
    mantis = get_object_or_404(Mantis, pk=mantis_id)
    return render(request, 'mantises/mantis_detail.html', {'mantis': mantis})


def breed_detail(request, breed_id):
    breed = get_object_or_404(Breed, pk=breed_id)
    return render(request, 'mantises/breed_detail.html', {'breed': breed})


@login_required
def mymantises(request):
    mantis_list = Mantis.objects.filter(user_id=request.user.id)
    context = {'mantis_list': mantis_list}
    return render(request, 'mantises/mymantises.html', context)


@login_required
def molt(request, mantis_id):
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

    return render(request, 'mantises/molt_history.html', {'history': history, 'mantis':mantis})