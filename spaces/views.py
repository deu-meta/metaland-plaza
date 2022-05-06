# Create your views here.
from articles.permissions import IsStaffOrReadOnly
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Space
from .serializers import SpaceSerializer


class SpaceViewSet(viewsets.ModelViewSet):
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsStaffOrReadOnly]
