from rest_framework import serializers

from likes.models import FanficLike, AnimeLike, MangaLike


class FanficLikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    fanfic = serializers.ReadOnlyField(source='fanfic.id')

    class Meta:
        model = FanficLike
        fields = '__all__'

class AnimeLikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    anime = serializers.ReadOnlyField(source='anime.id')

    class Meta:
        model = AnimeLike
        fields = '__all__'


class MangaLikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    manga = serializers.ReadOnlyField(source='manga.id')

    class Meta:
        model = MangaLike
        fields = '__all__'


