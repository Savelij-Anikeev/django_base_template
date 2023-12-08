from .models import ImageTestTable
from rest_framework import serializers


class ImageTestTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageTestTable
        fields = '__all__'
