# Create your views here.
from articles.permissions import IsStaffOrReadOnly
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from spaces.models import Spaces

from .serializers import SpaceSerializer


class SpaceViewSet(viewsets.ModelViewSet):
    queryset = Spaces.objects.all()
    serializer_class = SpaceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsStaffOrReadOnly]
