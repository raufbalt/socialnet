from django.contrib import admin

from .models import Manga, MangaVolume, MangaGenres, Chapter
admin.site.register(Manga)
admin.site.register(MangaVolume)
admin.site.register(MangaGenres)
admin.site.register(Chapter)