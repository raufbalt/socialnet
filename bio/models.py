from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()


class Biography(models.Model):
    about_me = models.CharField(max_length=255, blank=True, default=' ')
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.owner)

