from rest_framework import viewsets

from events.models import Person, Category, Event, Location, EventLocation
from .serializers import (
    PersonSerializer,
    CategorySerializer,
    LocationSerializer,
    EventReadSerializer,
    EventWriteSerializer,
    EventLocationReadSerializer,
    EventLocationWriteSerializer,
)


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PATCH', 'PUT']:
            return EventWriteSerializer
        return EventReadSerializer


class EventLocationViewSet(viewsets.ModelViewSet):
    queryset = EventLocation.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PATCH', 'PUT']:
            return EventLocationWriteSerializer
        return EventLocationReadSerializer
