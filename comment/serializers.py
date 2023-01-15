from rest_framework import serializers
from .models import FanficComment


class FanficCommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    fanfic = serializers.ReadOnlyField(source='fanfic.title')

    class Meta:
        model = FanficComment
        fields = '__all__'