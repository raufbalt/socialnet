from decouple import config
from django.shortcuts import render, get_object_or_404
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from comment.serializers import MangaCommentSerializer
from likes.serializers import MangaLikeSerializer
from .models import Manga, MangaVolume, MangaGenres, Chapter
from .serializers import MangaSerializer, MangaVolumeSerializer, MangaGenresSerializer, ChapterSerializer

from rest_framework.decorators import action
from rest_framework import permissions, response
from fanfic.views import clock

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class MangaGenresListAPIView(ListAPIView):
    queryset = MangaGenres.objects.all()
    serializer_class = MangaGenresSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = []

class MangaViewSet(ModelViewSet):
    serializer_class = MangaSerializer
    queryset = Manga.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('genre',)
    search_fields = ('title',)

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'delete', 'create'):
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticatedOrReadOnly()]

    def perform_create(self, serializer):
        data = self.request.data
        genre = self.request.data.get('genre', None)
        genre1 = get_object_or_404(MangaGenres, slug=genre)

        Manga.objects.create(

            title=data.get("title", None),
            genre=genre1,
            image=data.get("image", None),
            desc=data.get("desc", None)
        )

    @action(['GET'], detail=True)
    def volumes(self, request, pk):
        manga = self.get_object()
        if request.method == 'GET':
            volumes = manga.volumes.all()
            serializer = MangaVolumeSerializer(volumes, many=True)
            return response.Response(serializer.data, status=200)


    @action(['POST', 'DELETE'], detail=True)
    def likes(self, request, pk):
        manga = self.get_object()
        likes = manga.likes.all()
        data = request.data
        serializer = MangaLikeSerializer(data=data)
        if request.method == 'POST':
            if manga.likes.filter(owner=request.user).exists():
                return response.Response('Вы уже поставили лайк', status=400)
            serializer.is_valid(raise_exception=True)
            serializer.save(manga=manga, owner=self.request.user)
            return response.Response(serializer.data, status=201)
        if request.method == 'DELETE':
            delete_owner = self.request.user
            delete_likes = likes.filter(owner=delete_owner)
            serializer.is_valid(raise_exception=True)
            delete_likes.delete()
            return response.Response(serializer.data, status=204)

    @action(['POST', 'DELETE'], detail=True)
    def comment(self, request, pk):
        manga = self.get_object()
        commentaries = manga.comments.all()
        data = request.data
        serializer = MangaCommentSerializer(data=data)
        if request.method == 'POST':
            serializer.is_valid(raise_exception=True)
            serializer.save(manga=manga, owner=self.request.user, text=self.request.data.get('text', None),
                            date_created=clock(), owner_username=self.request.user.username, owner_image=str(config('Url'))+str(self.request.user.avatar))
            return response.Response(serializer.data, status=201)
        if request.method == 'DELETE':
            delete_id = self.request.data.get('id', None)
            delete_comment = commentaries.filter(id=delete_id)
            serializer.is_valid(raise_exception=True)
            delete_comment.delete()
            return response.Response(serializer.data, status=204)


class ChapterViewSet(ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'delete', 'create'):
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticatedOrReadOnly()]

