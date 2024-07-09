from django.contrib.auth.models import AbstractUser
from django.db import models

from eventy.constants import MAX_LENGTH_BIO_USER, MAX_LENGTH_LOCATION_USER, MAX_LENGTH_ROLE_USER


class Profile(AbstractUser):
    bio = models.TextField(max_length=MAX_LENGTH_BIO_USER, blank=True)
    location = models.CharField(max_length=MAX_LENGTH_LOCATION_USER, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=MAX_LENGTH_ROLE_USER, blank=True)

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_moderator(self):
        return self.role == 'moderator'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.username
