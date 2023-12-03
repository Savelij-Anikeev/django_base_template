from django.contrib import admin
from .models import Event, UserEventRel

admin.site.register(Event)
admin.site.register(UserEventRel)
