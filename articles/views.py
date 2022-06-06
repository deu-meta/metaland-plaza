# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from .permissions import IsUserOrReadOnly
from .serializers import *


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]
    filter_backends = [OrderingFilter, SearchFilter]

    ordering_fields = ["created_at"]
    search_fields = ["title"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, author_id=self.request.user.id)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, author_id=self.request.user.id)
