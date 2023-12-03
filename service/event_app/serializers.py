from rest_framework import serializers

from .models import Event, User, UserEventRel


class UserSerializer(serializers.ModelSerializer):
    """serializer for user model"""
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class EventSerializer(serializers.ModelSerializer):
    """serializer for event model"""
    class Meta:
        model = Event
        fields = '__all__'


class UserEventRelSerializer(serializers.ModelSerializer):
    """serializer for user and event relation"""
    class Meta:
        model = UserEventRel
        fields = '__all__'



