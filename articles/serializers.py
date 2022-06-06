from metaland.serializers import TokenUserSerializer
from rest_framework import serializers

from .models import *


class ArticleSerializer(serializers.ModelSerializer):
    author = TokenUserSerializer()

    class Meta:
        model = Article
        read_only_fields = ("author_id",)
        fields = ("id", "category", "title", "created_at", "contents", "author", "author_id")


class CommentSerializer(serializers.ModelSerializer):
    author = TokenUserSerializer()

    class Meta:
        model = Comment
        read_only_fields = ("author_id",)
        fields = ("id", "article", "created_at", "contents", "author", "author_id")
