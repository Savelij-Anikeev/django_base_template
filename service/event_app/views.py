from django.db.models import F
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer, EventSerializer, UserEventRelSerializer
from .models import Event, UserEventRel

from django.conf import settings
from .permissions import IsOwnerOrAdmin


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
    permission_classes = ()

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

    def get_permissions(self):
        if self.request.method not in ('GET', 'POST', 'HEAD', 'OPTIONS'):
            permission_classes = (IsAuthenticated, IsOwnerOrAdmin)
        else:
            permission_classes = ()
        return [permission() for permission in permission_classes]


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
        obj = get_object_or_404(UserEventRel,
                                event=get_object_or_404(Event, id=event_id),
                                user=self.request.user)
        return obj

    def perform_create(self, serializer):
        """automatically adding user"""
        curr_user = self.request.user
        curr_event = get_object_or_404(Event, id=self.request.data['event'])
        serializer.validated_data['user'] = curr_user
        serializer.validated_data['event'] = curr_event

        if len(UserEventRel.objects.filter(event=curr_event, user=curr_user)) != 0:
            return self.perform_update(serializer)
        serializer.save()

        Event.objects.filter(id=curr_event.id).update(free_places=F('free_places')-1)

    def perform_destroy(self, instance):
        instance.delete()
        Event.objects.filter(id=instance.event.id).update(free_places=F('free_places')+1)

    def get_queryset(self):
        """list only relation user in"""
        if self.request.user.is_authenticated:
            return UserEventRel.objects.filter(user=self.request.user)
        return UserEventRel.objects.none()
