from django.urls import path

from .views import (
    index,
    event_detail,
    get_categories,
    get_locations,
    get_people,
    person_detail,
    CreateEvent,
    CreateEventLocation,
)

app_name = 'events'

urlpatterns = [
    path('create_event_location/', CreateEventLocation.as_view(), name='create_event_location'),
    path('create/', CreateEvent.as_view(), name='create_event'),
    path('people/<int:person_id>/', person_detail, name='person_detail'),
    path('people/', get_people, name='people'),
    path('locations/', get_locations, name='locations'),
    path('categories/', get_categories, name='categories'),
    path('<int:event_id>/', event_detail, name='event_detail'),
    path('', index, name='index'),
]
