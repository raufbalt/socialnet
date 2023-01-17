from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.text import slugify


class Anime(models.Model):
    title = models.CharField(max_length=30, blank=True, unique=True)
    genre = models.ForeignKey('AnimeGenres', blank=True, default='Other', on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.title


class AnimeSeason(models.Model):
    slug = models.SlugField(max_length=50, primary_key=True)
    title = models.CharField(max_length=30, unique=True)
    own_anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='seasons')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Episode(models.Model):
    slug = models.SlugField(max_length=50, primary_key=True)
    title = models.CharField(max_length=30, unique=True)

    season = models.ForeignKey(AnimeSeason, on_delete=models.CASCADE, related_name='episodes')
    video = models.FileField(upload_to='media/', blank=True, null=True, validators=[FileExtensionValidator(['mp4'])])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class AnimeGenres(models.Model):
    slug = models.SlugField(max_length=50, primary_key=True)
    name = models.CharField(max_length=30, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

