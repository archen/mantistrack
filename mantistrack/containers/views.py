# Core Python imports

# Core Django imports
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView

# App-specific imports
from containers.models import Container, ContainerType, EnvironmentReading
from containers.forms import ContainerForm, ContainerTypeForm, EnvironmentReadingForm
from mantises.models import Mantis, Ooth


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
        form.instance.container_id = self.kwargs['container_id']
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
    readings = EnvironmentReading.objects.filter(container=container).order_by('-date')[:5]
    mantises = Mantis.objects.filter(container=container)
    ooths = Ooth.objects.filter(container=container)
    if request.user.id == container.user.id:
        notes = container.notes.all()
    else:
        notes = container.notes.filter(is_public=True)
    return render(request, 'containers/container_detail.html', {'container': container, 'mantises': mantises,
                                                                'readings': readings, 'ooths': ooths, 'notes': notes})


def detail_container_type(request, container_type_id):
    container_type = get_object_or_404(ContainerType, pk=container_type_id)
    if request.user.id == container_type.user.id:
        notes = container_type.notes.all()
    else:
        notes = container_type.notes.filter(is_public=True)
    return render(request, 'containers/container_type_detail.html', {'container_type': container_type, 'notes': notes})


def reading_history(request, container_id):
    container = get_object_or_404(Container, pk=container_id)
    history = EnvironmentReading.objects.filter(container=container)

    return render(request, 'containers/reading_history.html', {'container': container, 'history': history})


def detail_reading(request, container_id, pk):
    container = Container.objects.get(pk=container_id)
    reading = container.environmentreading_set.get(pk=pk)
    if request.user.id == reading.user.id:
        notes = reading.notes.all()
    else:
        notes = reading.notes.filter(is_public=True)
    return render(request, 'containers/reading_detail.html', {'reading': reading, 'notes': notes})