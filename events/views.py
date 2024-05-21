from django.shortcuts import render, get_object_or_404

from .models import Event, Category, Person, Location


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
    people = Person.objects.all()
    return render(request, 'events/people.html', {'people': people})


def person_detail(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    return render(request, 'events/person_detail.html', {'person': person})
