from django.urls import path

from .views import index, event_detail

app_name = 'events'

urlpatterns = [
    path('<int:event_id>/', event_detail, name='event_detail'),
    path('', index, name='index'),
]
