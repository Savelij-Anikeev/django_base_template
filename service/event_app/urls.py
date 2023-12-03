from rest_framework import routers

from django.urls import path
from .views import UserViewSet, EventViewSet, UserEventRelViewSet


router = routers.SimpleRouter()
router.register('users', UserViewSet)
router.register('events', EventViewSet)
router.register('events', UserEventRelViewSet)

urlpatterns = []

urlpatterns += router.urls

