from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .serializer import BiographySerializer
from .models import Biography
from fanfic.permissions import IsOwner


class BioViewSet(ModelViewSet):
    serializer_class = BiographySerializer
    queryset = Biography.objects.all()

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'delete'):
            return [IsOwner()]
        elif self.action == 'create':
            return [permissions.IsAuthenticated()]
        return [permissions.IsAuthenticatedOrReadOnly()]