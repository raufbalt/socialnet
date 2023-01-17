from django.contrib import admin

from .models import Anime, AnimeSeason, Episode, AnimeGenres

admin.site.register(Anime)
admin.site.register(AnimeSeason)
admin.site.register(Episode)
admin.site.register(AnimeGenres)
