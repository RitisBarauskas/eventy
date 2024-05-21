from django.db.models import Count, Subquery, OuterRef
from django.forms import IntegerField
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Event, Category, Person, Location, EventLocation
from .forms import EventLocationForm


def index(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', {'events': events})


def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/event_detail.html', {'event': event})


def get_categories(request):
    categories = Category.objects.all()
    return render(request, 'events/categories.html', {'categories': categories})


def get_locations(request):
    locations = Location.objects.all()
    return render(request, 'events/locations.html', {'locations': locations})


def get_people(request):
    people = Person.objects.annotate(events_count=Count('events__places'))
    return render(request, 'events/people.html', {'people': people})


def person_detail(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    return render(
        request,
        'events/person_detail.html',
        {'person': person},
    )


class CreateEvent(CreateView):
    model = Event
    fields = ['name', 'description', 'category', 'participants']
    template_name = 'events/create_event.html'

    def get_success_url(self):
        return reverse_lazy('events:event_detail', kwargs={'event_id': self.object.id})


class CreateEventLocation(CreateView):
    model = EventLocation
    template_name = 'events/create_event_location.html'
    form_class = EventLocationForm

    def get_success_url(self):
        return reverse_lazy('events:event_detail', kwargs={'event_id': self.object.event_id})