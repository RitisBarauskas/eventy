import factory
from factory.django import DjangoModelFactory

from events.models import Category, Event, Location, Person, EventLocation


class PersonFactory(DjangoModelFactory):
    class Meta:
        model = Person

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    description = factory.Faker('text')


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')


class EventFactory(DjangoModelFactory):
    class Meta:
        model = Event

    name = factory.Faker('word', locale='ru_RU')
    description = factory.Faker('text', locale='ru_RU')
    category = factory.SubFactory(CategoryFactory)

    @classmethod
    def create(cls, **kwargs):
        participants = kwargs.pop('participants', [])
        event = super().create(**kwargs)

        if not participants:
            participants = PersonFactory.create_batch(5)

        event.participants.set(participants)
        return event
