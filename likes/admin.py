from django.contrib import admin

from .models import FanficLike, MangaLike

admin.site.register(FanficLike)
admin.site.register(MangaLike)