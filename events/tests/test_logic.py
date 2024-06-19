from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from events.models import Category, Event, Location, Person, EventLocation
from events.factories import EventFactory


User = get_user_model()


class TestLogic(TestCase):

    INDEX_URL = reverse('events:index')

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='test', password='test')
        cls.category_concert = Category.objects.create(name='Концерт')
        cls.location_arena = Location.objects.create(name='Арена', city='Москва', address='ул. Ленина, 1', capacity=1000)
        cls.dj_python = Person.objects.create(first_name='Джанго', last_name='Питон', description='DJ')
        cls.events = EventFactory.create_batch(100, participants=[cls.dj_python], category=cls.category_concert)

        cls.event_location_arena = EventLocation.objects.create(
            event=cls.events[0],
            location=cls.location_arena,
            date=datetime.now().date(),
            time=datetime.now().time(),
            price=1000,
        )
        cls.event_detail_url = reverse('events:event_detail', args=[cls.events[0].id])

    def setUp(self):
        super().setUp()
        self.user_client = Client()
        self.user_client.force_login(self.user)

    def test_index(self):
        response = self.client.get(self.INDEX_URL)
        self.assertEqual(response.status_code, 200)
        events = response.context.get('events')
        self.assertIsNotNone(events)
        self.assertEqual(events.count(), len(self.events))
        sorted_events = sorted(self.events, key=lambda event: event.name)
        self.assertEqual(list(events), sorted_events)
        # self.assertEqual(events[0].name, self.event_concert.name)
        # self.assertEqual(events[0].description, self.event_concert.description)
        # self.assertEqual(events[0].category, self.event_concert.category)
        participant_ids = list(events[0].participants.values_list('id', flat=True))
        self.assertIn(self.dj_python.id, participant_ids)

    def test_event_detail(self):
        response = self.client.get(self.event_detail_url)
        self.assertEqual(response.status_code, 200)
