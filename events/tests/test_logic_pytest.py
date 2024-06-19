from http import HTTPStatus

from events.tests.conftest import NAME_EVENT_CREATE, DESCRIPTION_EVENT_CREATE
from events.models import Event


def test_create_event(init_db, dj_php, dj_python, categories, create_event_url, client):
    event_ids_before = set(Event.objects.values_list('id', flat=True))
    form_data = {
        'name': NAME_EVENT_CREATE,
        'description': DESCRIPTION_EVENT_CREATE,
        'category': categories[0].id,
        'participants': [dj_php.id, dj_python.id],
    }
    response = client.post(create_event_url, data=form_data)
    assert response.status_code == HTTPStatus.FOUND
    event_ids_after = set(Event.objects.values_list('id', flat=True))
    diff_ids = event_ids_after - event_ids_before

    assert len(diff_ids) == 1
    event = Event.objects.get(id=diff_ids.pop())
    assert event.name == NAME_EVENT_CREATE
    assert event.description == DESCRIPTION_EVENT_CREATE
    assert event.category.id == form_data['category']
    assert sorted(list(event.participants.values_list('id', flat=True))) == sorted(form_data['participants'])
