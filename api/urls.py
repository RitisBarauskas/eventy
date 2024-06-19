from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PersonViewSet, CategoryViewSet, LocationViewSet, EventViewSet, EventLocationViewSet

router_v1 = DefaultRouter()
router_v1.register('persons', PersonViewSet, basename='person')
router_v1.register('categories', CategoryViewSet, basename='category')
router_v1.register('locations', LocationViewSet, basename='location')
router_v1.register('events', EventViewSet, basename='event')
router_v1.register('event-locations', EventLocationViewSet, basename='event_location')

urlpatterns = [
    path('v1/', include(router_v1.urls), name='v1'),
]
