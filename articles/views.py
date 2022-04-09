# Create your views here.
from rest_framework import permissions, status, viewsets

from .permissions import IsUserOrReadOnly
from .serializers import *


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]
    queryset = Comments.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
