from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from news.models import News
from news.serializers import NewsSerializer


class NewsViewSet(ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'delete', 'create'):
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticatedOrReadOnly()]

    def perform_create(self, serializer):
        data = self.request.data

        News.objects.create(

            title=data.get("title", None),
            video=data.get("video", None),
            image=data.get("image", None),
            text=data.get("text", None)
        )