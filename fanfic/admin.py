from django.contrib import admin

from .models import FanficGenres, Fanfic, FanficPage

admin.site.register(FanficGenres)
admin.site.register(Fanfic)
admin.site.register(FanficPage)