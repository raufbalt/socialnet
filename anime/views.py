
from rest_framework import permissions, response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

from .models import Anime, AnimeSeason, Episode, AnimeGenres
from .serializers import AnimeSerializer, EpisodeSerializer, SeasonSerializer

class AnimeViewSet(ModelViewSet):
    serializer_class = AnimeSerializer
    queryset = Anime.objects.all()

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'delete', 'create'):
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticatedOrReadOnly()]

    def perform_create(self, serializer):
        data = self.request.data
        genre = self.request.data.get('genre', None)
        genre1 = get_object_or_404(AnimeGenres, slug=genre)

        Anime.objects.create(

            title=data.get("title", None),
            genre=genre1
        )

    @action(['GET', 'POST'], detail=True)
    def season(self, request, pk):
        anime = self.get_object()
        if request.method == 'GET':
            seasons = anime.seasons.all()
            serializer = SeasonSerializer(seasons, many=True)
            return response.Response(serializer.data, status=200)
        data = request.data
        serializer = SeasonSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(own_anime=anime, slug=self.request.data.get('slug', None),
                        title=self.request.data.get("title", None), )
        return response.Response(serializer.data, status=201)


class EpisodeViewSet(ModelViewSet):
    serializer_class = EpisodeSerializer
    queryset = Episode.objects.all()

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'delete', 'create'):
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticatedOrReadOnly()]

    def perform_create(self, serializer):
        data = self.request.data
        season = self.request.data.get('season', None)
        season1 = get_object_or_404(AnimeSeason, slug=season)

        Episode.objects.create(

            title=data.get("title", None),
            slug=data.get("slug", None),
            season=season1,
        )







