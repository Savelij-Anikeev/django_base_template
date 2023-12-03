from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer, EventSerializer, UserEventRelSerializer
from .models import Event, UserEventRel

from django.conf import settings


# Ready to use
class UserViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    crud operations with `Event` model
    """
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


# In dev process:
class UserEventRelViewSet(viewsets.ModelViewSet):
    """
    describes behavior of relations between
    `User` and `Event`
    """
    queryset = UserEventRel.objects.all()
    serializer_class = UserEventRelSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        """finding relation by `Event` id"""
        event_id = self.kwargs['pk']
        return get_object_or_404(UserEventRel, user=self.request.user,
                                 event=Event.objects.get(pk=event_id))

    def perform_create(self, serializer):
        """automatically adding user"""
        serializer.validated_data['user'] = self.request.user
        serializer.save()

    def get_queryset(self):
        """list only relation user in"""
        if self.request.user.is_authenticated:
            return UserEventRel.objects.filter(user=self.request.user)
        return UserEventRel.objects.none()
