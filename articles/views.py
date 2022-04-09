# Create your views here.
from rest_framework import permissions, status, viewsets

from .serializers import *


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Articles.objects.filter(author=user)

        return queryset
