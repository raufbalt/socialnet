from rest_framework import serializers
from .models import FanficComment, MangaComment

class FanficCommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    fanfic = serializers.ReadOnlyField(source='fanfic.title')

    class Meta:
        model = FanficComment
        fields = '__all__'


class MangaCommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    manga = serializers.ReadOnlyField(source='manga.title')

    class Meta:
        model = MangaComment
        fields = '__all__'