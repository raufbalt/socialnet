from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

from .views import BioViewSet

router = DefaultRouter()
router.register('biography', BioViewSet)

urlpatterns = [
    path('', include(router.urls))
]