from datacenter.models import Passcard, Visit, get_duration, is_visit_long

from django.shortcuts import render


def storage_information_view(request):
    not_leaved_visitors = Visit.objects.filter(leaved_at = None)
    non_closed_visits = []
    for not_leaved_visitor in not_leaved_visitors:
        entered_at = not_leaved_visitor.entered_at
        duration = get_duration(not_leaved_visitor)
        name = not_leaved_visitor.passcard
        stat_non_closed_visits = {
            'who_entered': name,
            'entered_at': entered_at,
            'duration': duration,
            'is_strange': is_visit_long(not_leaved_visitor)
        }
        non_closed_visits.append(stat_non_closed_visits)
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
