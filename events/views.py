from django.http import HttpResponse
from django.shortcuts import render

from .database import DB


def index(request):
    events = DB.get('events', [])
    return render(request, 'index.html', {'events': events})


def event_detail(request, event_id):
    event = next((
        event for event in DB.get('events', [])
        if event.get('id') == event_id
    ), None)
    if not event:
        return HttpResponse('Event not found', status=404)

    return render(request, 'event_detail.html', {'event': event})
