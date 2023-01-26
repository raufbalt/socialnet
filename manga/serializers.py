from rest_framework import serializers

from .models import Manga, MangaVolume, MangaGenres, Chapter, MangaImages

class MangaImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MangaImages
        fields = '__all__'
class MangaGenresSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()

    class Meta:
        model = MangaGenres
        fields = ['slug', 'title']


class MangaVolumeSerializer(serializers.ModelSerializer):
    own_manga = serializers.ReadOnlyField(source='manga.title')

    class Meta:
        model = MangaVolume
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        try:
            rep['chapters'] = instance.chapters.all().values()
        except AttributeError:
            rep['chapters'] = 'null'
            return rep
        return rep


class MangaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manga
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        try:
            rep['likes'] = instance.likes.all().count()
        except AttributeError:
            rep['likes'] = 0
        try:
            rep['volumes'] = instance.volumes.all().values()
        except AttributeError:
            rep['volumes'] = 'none'
        try:
            rep['commentaries'] = instance.comments.all().values()
            rep['commentaries_count'] = instance.comments.all().count()
        except AttributeError:
            rep['commentaries'] = 'Нет комментариев к публикации'
            rep['commentaries_count'] = 0
            return rep
        return rep


class ChapterSerializer(serializers.ModelSerializer):
    volume = serializers.ReadOnlyField(source='volume.title')

    class Meta:
        model = Chapter
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        try:
            rep['images'] = instance.images.all().values()
        except AttributeError:
            rep['images'] = 'null'
            return rep
        return rep