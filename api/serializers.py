from rest_framework import serializers

import settings
from events.models import Person, Category, Event, Location, EventLocation


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class EventReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    participants = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Event
        fields = '__all__'


class EventWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def validate_participants(self, participants):
        if len(participants) < settings.MIN_COUNT_EVENT_PARTICIPANTS:
            raise serializers.ValidationError(
                f'Минимальное количество участников - {settings.MIN_COUNT_EVENT_PARTICIPANTS}'
            )

        return participants

    def to_representation(self, instance):
        return EventReadSerializer(instance).data


class EventLocationReadSerializer(serializers.ModelSerializer):
    event = EventReadSerializer()
    location = LocationSerializer()
    class Meta:
        model = EventLocation
        fields = '__all__'


class EventLocationWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLocation
        fields = '__all__'

    def to_representation(self, instance):
        return EventLocationReadSerializer(instance).data
