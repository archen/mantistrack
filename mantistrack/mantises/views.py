from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.utils import IntegrityError
from datetime import datetime

from mantises.models import Mantis, Molt


def index(request):
    top_mantis_list = Mantis.objects.order_by('-name')[:5]
    context = {'top_mantis_list': top_mantis_list}
    return render(request, 'mantises/index.html', context)


def detail(request, mantis_id):
    mantis = get_object_or_404(Mantis, pk=mantis_id)
    return render(request, 'mantises/detail.html', {'mantis': mantis})


@login_required
def molt(request, mantis_id):
    mantis = get_object_or_404(Mantis, pk=mantis_id)

    try:
        molt_record = Molt(mantis_id=mantis.id, user_id=request.user.id, date=datetime.now(mantis.born.tzinfo),
                           from_instar=mantis.instar(), to_instar=mantis.instar()+1)
        molt_record.save()
    except IntegrityError:
        return render(request, 'mantises/detail.html', {
            'mantis': mantis,
            'error_message': 'Error saving molt record.',
        })

    return render(request, 'mantises/detail.html', {'mantis': mantis})