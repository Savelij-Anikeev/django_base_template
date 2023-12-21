from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Event(models.Model):
    """describes db fields of event"""
    # organizers info
    username = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=11)
    social_links = models.CharField(max_length=128)
    organization = models.CharField(max_length=128)

    # event info
    event_name = models.CharField(max_length=128)
    event_type = models.CharField(max_length=128)
    event_date = models.CharField(max_length=12)
    event_time = models.CharField(max_length=5)
    event_place = models.CharField(max_length=128)

    # additional fields
    is_verified = models.BooleanField(default=False)
    photo = models.ImageField(null=True, blank=True)
    photo_url = models.CharField(max_length=1024, null=True, blank=True, default=settings.DEFAULT_IMG_URL)

    # places
    is_place_limited = models.BooleanField(default=False)
    places = models.PositiveIntegerField(default=0, null=True, blank=True)
    free_places = models.PositiveIntegerField(default=0, null=True, blank=True)

    # category
    category = models.ManyToManyField('Category', null=True, blank=True)


class UserEventRel(models.Model):
    """
    describes db fields of `Even` and `User` relation
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class Category(models.Model):
    """
    category table for events
    """
    name = models.CharField(max_length=32)

