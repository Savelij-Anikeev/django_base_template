from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, EventSerializer, UserEventRelSerializer
from .models import Event, UserEventRel

from django.conf import settings


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EventViewSet(viewsets.ModelViewSet):
    """crud with `Event` model"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        """changing photo if it is not there"""
        if serializer.validated_data['photo'] == '':
            serializer.validated_data['photo'] = settings.DEFAULT_IMG_URL
        serializer.save()

    def get_queryset(self):
        """return queryset"""
        if 'is_verified' in self.request.GET:
            """looking for get param"""
            if self.request.GET['is_verified'] == 'False':
                return Event.objects.filter(is_verified=False)
            if self.request.GET['is_verified'] == 'all':
                return Event.objects.all()
        return Event.objects.filter(is_verified=True)


class UserEventRelViewSet(viewsets.ModelViewSet):
    queryset = UserEventRel.objects.all()
    serializer_class = UserEventRelSerializer

