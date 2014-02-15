# Core Python imports
from datetime import datetime

# Core Django imports
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.utils import IntegrityError
from django.views.generic.edit import CreateView, UpdateView

# App-specific imports
from containers.models import Container, ContainerType, EnvironmentReading
from containers.forms import ContainerForm, ContainerTypeForm, EnvironmentReadingForm
from mantises.models import Mantis


class ContainerCreate(CreateView):
    model = Container
    form_class = ContainerForm

    def get_form(self, form_class):
        form = super(ContainerCreate, self).get_form(form_class)
        form.instance.user_id = self.request.user.id
        return form


class ContainerUpdate(UpdateView):
    model = Container
    form_class = ContainerForm


class ContainerTypeCreate(CreateView):
    model = ContainerType
    form_class = ContainerTypeForm

    def get_form(self, form_class):
        form = super(ContainerTypeCreate, self).get_form(form_class)
        form.instance.user_id = self.request.user.id
        return form


class ContainerTypeUpdate(UpdateView):
    model = ContainerType
    form_class = ContainerTypeForm


class EnvironmentReadingCreate(CreateView):
    model = EnvironmentReading
    form_class = EnvironmentReadingForm

    def get_form(self, form_class):
        form = super(EnvironmentReadingCreate, self).get_form(form_class)
        form.instance.user_id = self.request.user.id
        return form


class EnvironmentReadingUpdate(UpdateView):
    model = EnvironmentReading
    form_class = EnvironmentReadingForm


def index(request):
    container_list = Container.objects.all()
    container_type_list = ContainerType.objects.all()
    context = {'container_list': container_list, 'container_type_list': container_type_list}
    return render(request, 'containers/index.html', context)


def containers(request):
    container_list = Container.objects.all()
    context = {'container_list': container_list}
    return render(request, 'containers/containers.html', context)


def container_types(request):
    container_type_list = ContainerType.objects.all()
    context = {'container_type_list': container_type_list}
    return render(request, 'containers/container_types.html', context)


def my_containers(request):
    container_list = Container.objects.filter(user_id=request.user.id)
    context = {'container_list': container_list}
    return render(request, 'containers/my_containers.html', context)


def my_container_types(request):
    container_type_list = ContainerType.objects.filter(user_id=request.user.id)
    context = {'container_type_list': container_type_list}
    return render(request, 'containers/my_container_types.html', context)


def detail_container(request, container_id):
    container = get_object_or_404(Container, pk=container_id)
    mantises = Mantis.objects.filter(container=container)
    return render(request, 'containers/container_detail.html', {'container': container, 'mantises': mantises})


def detail_container_type(request, container_type_id):
    container_type = get_object_or_404(ContainerType, pk=container_type_id)
    return render(request, 'containers/container_type_detail.html', {'container_type': container_type})


def reading_history(request, container_id):
    container = get_object_or_404(Container, container_id)
    history = EnvironmentReading.objects.filter(container=container)

    return render(request, 'containers/reading-history.html', {'container': container, 'history':history})