from metaland.serializers import TokenUserSerializer
from rest_framework import serializers

from .models import *


class ArticleSerializer(serializers.ModelSerializer):
    author = TokenUserSerializer()

    class Meta:
        model = Article
        fields = ("id", "category", "title", "created_at", "contents", "author")


class CommentSerializer(serializers.ModelSerializer):
    author = TokenUserSerializer()

    class Meta:
        model = Comment
        fields = ("id", "article", "created_at", "contents", "author")
