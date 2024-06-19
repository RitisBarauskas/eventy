import pytest
from django.urls import reverse

from events.models import Person, Category, Event
from events.factories import PersonFactory, CategoryFactory

NAME_EVENT_CREATE = 'Создание события'
DESCRIPTION_EVENT_CREATE = 'Описание события'


@pytest.fixture()
def dj_python():
    return PersonFactory.create(first_name='Джанго')


@pytest.fixture()
def dj_php():
    return PersonFactory.create(first_name='PHP')


@pytest.fixture()
def categories():
    return CategoryFactory.create_batch(10)


@pytest.fixture()
def index_url():
    return reverse('events:index')


@pytest.fixture()
def create_event_url():
    return reverse('events:create_event')


@pytest.fixture(autouse=True)
def init_db(db, dj_python, dj_php, categories):
    event = Event.objects.create(name='Концерт Джа Пыха', description='Концерт Джа Пыха', category=categories[0])
    event.participants.add(dj_python)
