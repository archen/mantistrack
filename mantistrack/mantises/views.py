from django.shortcuts import render, get_object_or_404

from mantises.models import Mantis


def index(request):
    top_mantis_list = Mantis.objects.order_by('-name')[:5]
    context = {'top_mantis_list': top_mantis_list}
    return render(request, 'mantises/index.html', context)


def detail(request, mantis_id):
    mantis = get_object_or_404(Mantis, pk=mantis_id)
    return render(request, 'mantises/detail.html', {'mantis': mantis})