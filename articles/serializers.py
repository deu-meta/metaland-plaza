from rest_framework import serializers

from .models import *


class ArticleSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source="user.nickname")

    class Meta:
        model = Articles
        fields = ("id", "category", "title", "created_at", "contents", "author")


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="user.nickname")

    class Meta:
        model = Comments
        fields = ("id", "article", "created_at", "contents", "author")
