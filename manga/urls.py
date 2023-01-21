from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

from .views import MangaViewSet, ChapterViewSet

router = DefaultRouter()
router.register('manga', MangaViewSet)
router.register('mangachapter', ChapterViewSet)

urlpatterns = [
    path('mangagenres/', views.MangaGenresListAPIView.as_view()),
    path('', include(router.urls))
]