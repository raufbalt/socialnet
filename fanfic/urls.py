from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

from .views import FanficViewSet

router = DefaultRouter()
router.register('fanfic', FanficViewSet)

urlpatterns = [
    path('fanficgenres/', views.FanficGenresListAPIView.as_view()),
    path('', include(router.urls))
]