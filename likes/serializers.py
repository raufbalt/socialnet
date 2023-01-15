from rest_framework import serializers

from likes.models import FanficLike


class FanficLikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    fanfic = serializers.ReadOnlyField(source='fanfic.id')

    class Meta:
        model = FanficLike
        fields = '__all__'