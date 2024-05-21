from django.contrib import admin


from .models import Event, Category, Person, Location, EventLocation

admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Person)
admin.site.register(Location)
admin.site.register(EventLocation)
