from rest_framework import serializers
from .models import Episode, Anime, AnimeSeason, AnimeGenres


class AnimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Anime
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        try:
            rep['seasons'] = instance.seasons.all().values()
        except AttributeError:
            rep['seasons'] = 0
        try:
            rep['likes'] = instance.likes.all().count()
        except AttributeError:
            rep['likes'] = 0
        return rep


class SeasonSerializer(serializers.ModelSerializer):
    own_anime = serializers.ReadOnlyField(source='anime.title')

    class Meta:
        model = AnimeSeason
        fields = "__all__"


class EpisodeSerializer(serializers.ModelSerializer):
    season = serializers.ReadOnlyField(source='season.title')
    anime = serializers.ReadOnlyField(source='anime.title')

    class Meta:
        model = Episode
        fields = "__all__"


class AnimeGenresSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()

    class Meta:
        model = AnimeGenres
        fields = ['slug']
