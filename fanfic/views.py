from django.shortcuts import get_object_or_404
from requests import Response
from rest_framework import permissions, response
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from fanfic.models import FanficGenres, Fanfic
from fanfic.permissions import IsOwner
from fanfic.serializers import FanficGenresSerializer, FanficSerializer, FanficPageSerializer

from likes.serializers import FanficLikeSerializer
from likes.models import FanficLike


class FanficGenresListAPIView(ListAPIView):
    queryset = FanficGenres.objects.all()
    serializer_class = FanficGenresSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = []


class FanficViewSet(ModelViewSet):
    serializer_class = FanficSerializer
    queryset = Fanfic.objects.all()

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'delete'):
            return [IsOwner()]
        elif self.action == 'create':
            return [permissions.IsAuthenticated()]
        return [permissions.IsAuthenticatedOrReadOnly()]

    def perform_create(self, serializer):
        data = self.request.data

        genre = self.request.data.get('genre', None)
        genre1 = get_object_or_404(FanficGenres, slug=genre)

        Fanfic.objects.create(

            owner=self.request.user,
            title = self.request.data.get("title", None),
            genre = genre1,
	        description = self.request.data.get("description", None),
            image = self.request.data.get("image", None)
)

    @action(['GET', 'POST'], detail=True)
    def pages(self, request, pk):
        fanfic = self.get_object()
        if request.method == 'GET':
            pages = fanfic.page.all()
            serializer = FanficPageSerializer(pages, many=True)
            return response.Response(serializer.data, status=200)
        data = request.data
        serializer = FanficPageSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(fanfic=fanfic, text=self.request.data.get('text', None), owner=self.request.user)
        return response.Response(serializer.data, status=201)

    @action(['POST', 'DELETE'], detail=True)
    def likes(self, request, pk):
        fanfic = self.get_object()
        likes = fanfic.likes.all()
        data = request.data
        serializer = FanficLikeSerializer(data=data)
        if request.method == 'POST':
            serializer.is_valid(raise_exception=True)
            serializer.save(fanfic=fanfic, owner=self.request.user)
            return response.Response(serializer.data, status=201)
        if request.method == 'DELETE':
            delete_owner = self.request.user
            delete_likes = likes.filter(owner=delete_owner)
            serializer.is_valid(raise_exception=True)
            delete_likes.delete()
            return response.Response(serializer.data, status=204)



