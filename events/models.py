from django.db.models import (
    Model,
    CharField,
    PositiveSmallIntegerField,
    ForeignKey,
    DateField,
    TimeField,
    ManyToManyField,
    CASCADE,
)


class Person(Model):
    first_name = CharField(max_length=100, verbose_name='Имя')
    last_name = CharField(max_length=100, verbose_name='Фамилия')
    description = CharField(max_length=500, verbose_name='Описание')

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Category(Model):
    name = CharField(max_length=100, verbose_name='Название')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Event(Model):
    name = CharField(max_length=100, verbose_name='Название')
    description = CharField(max_length=500, verbose_name='Описание')
    category = ForeignKey(Category, on_delete=CASCADE, verbose_name='Категория', related_name='events')
    participants = ManyToManyField(Person, verbose_name='Участники', related_name='events')

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
        ordering = ['name']

    def __str__(self):
        return self.name


class Location(Model):
    name = CharField(max_length=100, verbose_name='Название')
    city = CharField(max_length=100, verbose_name='Город')
    address = CharField(max_length=500, verbose_name='Адрес')
    capacity = PositiveSmallIntegerField(verbose_name='Вместимость')

    class Meta:
        verbose_name = 'Место проведения'
        verbose_name_plural = 'Места проведения'

    def __str__(self):
        return f'{self.name} ({self.city})'


class EventLocation(Model):
    event = ForeignKey(Event, on_delete=CASCADE, verbose_name='Событие', related_name='places')
    location = ForeignKey(Location, on_delete=CASCADE, verbose_name='Место проведения', related_name='events')
    date = DateField(verbose_name='Дата')
    time = TimeField(verbose_name='Время')
    price = PositiveSmallIntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Место и время проведения'
        verbose_name_plural = 'Места и время проведения'

    def __str__(self):
        return f'{self.event} ({self.location})'
