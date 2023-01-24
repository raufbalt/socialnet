from rest_framework import serializers
from fanfic.models import FanficGenres, Fanfic, FanficPage


class FanficGenresSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()

    class Meta:
        model = FanficGenres
        fields = ['slug']


class FanficSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Fanfic
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        try:
            rep['likes'] = instance.likes.all().count()
        except AttributeError:
            rep['likes'] = 0
        try:
            rep['page'] = instance.page.all().values()
        except AttributeError:
            rep['page'] = 'none'
        try:
            rep['commentaries'] = instance.comments.all().values()
            rep['commentaries_count'] = instance.comments.all().count()
        except AttributeError:
            rep['commentaries'] = 'Нет комментариев к публикации'
            rep['commentaries_count'] = 0
            return rep
        return rep

class FanficPageSerializer(serializers.ModelSerializer):
    fanfic = serializers.ReadOnlyField(source='fanfic.title')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = FanficPage
        fields = '__all__'