from django.db import models

from django.contrib.auth import get_user_model

from fanfic.models import Fanfic

User = get_user_model()

class FanficLike(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    fanfic = models.ForeignKey(Fanfic, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f'{self.owner} -> {self.fanfic}'