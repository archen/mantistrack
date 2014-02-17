# Core Python imports

# Core Django imports
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView

# App-specific imports
from feeders.models import Feeder, Feeding, Hatch, Batch
from feeders.forms import FeederForm, FeedingForm, HatchForm, BatchForm


class FeederCreate(CreateView):
    model = Feeder
    form_class = FeederForm

    def get_form(self, form_class):
        form = super(FeederCreate, self).get_form(form_class)
        form.instance.user_id = self.request.user.id
        return form


class FeederUpdate(UpdateView):
    model = Feeder
    form_class = FeederForm


class FeedingCreate(CreateView):
    model = Feeding
    form_class = FeedingForm

    def get_form(self, form_class):
        form = super(FeedingCreate, self).get_form(form_class)
        form.instance.user_id = self.request.user.id
        return form


class FeedingUpdate(UpdateView):
    model = Feeding
    form_class = FeedingForm


class HatchCreate(CreateView):
    model = Hatch
    form_class = HatchForm

    def get_form(self, form_class):
        form = super(HatchCreate, self).get_form(form_class)
        form.instance.user_id = self.request.user.id
        return form


class HatchUpdate(UpdateView):
    model = Hatch
    form_class = HatchForm


class BatchCreate(CreateView):
    model = Batch
    form_class = BatchForm

    def get_form(self, form_class):
        form = super(BatchCreate, self).get_form(form_class)
        form.instance.user_id = self.request.user.id

        return form


class BatchUpdate(UpdateView):
    model = Batch
    form_class = BatchForm


def index(request):
    feeder_list = Feeder.objects.all()
    batch_list = Batch.objects.all()
    context = {'feeder_list': feeder_list, 'batch_list': batch_list}

    return render(request, 'feeders/index.html', context)


def feeders(request):
    feeder_list = Feeder.objects.all()
    context = {'feeder_list': feeder_list}

    return render(request, 'feeders/feeders.html', context)


def my_feeders(request):
    feeder_list = Feeder.objects.filter(user_id=request.user.id)
    context = {'feeder_list': feeder_list}

    return render(request, 'feeders/feeders.html', context)


def my_batches(request):
    batch_list = Batch.objects.filter(user_id=request.user.id)
    context = {'batch_list': batch_list}

    return render(request, 'feeders/my_batches.html', context)


def detail_feeder(request, feeder_id):
    feeder = get_object_or_404(Feeder, pk=feeder_id)

    return render(request, 'feeders/feeder_detail.html', {'feeder': feeder})


def hatch_history(request, batch_id):
    batch = get_object_or_404(Batch, pk=batch_id)
    history = Hatch.objects.filter(hatched_from=batch)

    return render(request, 'feeders/hatch_history.html', {'batch': batch, 'history': history})


def detail_batch(request, feeder_id, batch_id):
    batch = get_object_or_404(Batch, pk=batch_id)

    return render(request, 'feeders/batch_detail.html', {'batch': batch})