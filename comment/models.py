from decouple import config
from django.db import models
from fanfic.models import Fanfic
from manga.models import Manga
from django.contrib.auth import get_user_model
User = get_user_model()

class FanficComment(models.Model):
    fanfic = models.ForeignKey(Fanfic, on_delete=models.CASCADE, related_name='comments')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    owner_image = models.ImageField(null=True)
    owner_username = models.CharField(blank=True, null=True, max_length=30)
    text = models.CharField(max_length=255, null=True, default='cool!')

    date_created = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return f'{self.owner} - {self.text} -> {self.fanfic}'


class MangaComment(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name='comments')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    owner_image = models.ImageField(null=True)
    owner_username = models.CharField(blank=True, null=True, max_length=30)

    text = models.CharField(max_length=255, null=True, default='cool!')
    date_created = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return f'{self.owner} - {self.text} -> {self.manga}'
