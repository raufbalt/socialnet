from rest_framework import serializers

from likes.models import FanficLike, AnimeLike


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