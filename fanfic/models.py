from django.db import models
from django.utils.text import slugify

from django.core.validators import FileExtensionValidator

from django.contrib.auth import get_user_model
User = get_user_model()


class FanficGenres(models.Model):
    slug = models.SlugField(max_length=50, primary_key=True)
    name = models.CharField(max_length=30, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Fanfic(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=30, unique=True)
    image = models.FileField(upload_to='media/', blank=True, null=True, validators=[FileExtensionValidator('jpg')])
    description = models.CharField(max_length=255, blank=True, default='there is not any description')
    genre = models.ForeignKey(FanficGenres, blank=True, default='Other', on_delete=models.SET_DEFAULT)
    date_created = models.CharField(max_length=25, null=True, blank=True)
    def __str__(self):
        return self.title


class FanficPage(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fanfic = models.ForeignKey(Fanfic, on_delete=models.CASCADE, related_name='page')
    chapter = models.CharField(max_length=20, blank=True, default='Глава')
    text = models.CharField(max_length=1000, null=True)