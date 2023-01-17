from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

from .views import AnimeViewSet, EpisodeViewSet

router = DefaultRouter()
router.register('anime', AnimeViewSet)
router.register('episode', EpisodeViewSet)

urlpatterns = [
    path('', include(router.urls))
]