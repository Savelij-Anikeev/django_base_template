from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import ImageTestTable
from .serializers import ImageTestTableSerializer
from .storage_scripts import upload_event, test_script


class ImageTestTableViewSet(viewsets.ModelViewSet):
    queryset = ImageTestTable.objects.all()
    serializer_class = ImageTestTableSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response({'detail': 'created'}, status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        obj = serializer.save()
        upload_event.delay(obj.id)
