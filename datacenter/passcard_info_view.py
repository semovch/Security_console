from datacenter.models import Passcard, Visit, get_duration, is_visit_long

from django.shortcuts import render, get_object_or_404

from django.http import Http404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    this_passcard_visits = []
    for visit in Visit.objects.filter(passcard=passcard):
        visit_stat = {
            'entered_at': visit.entered_at,
            'duration': get_duration(visit),
            'is_strange': is_visit_long(visit)
        }
        this_passcard_visits.append(visit_stat)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
