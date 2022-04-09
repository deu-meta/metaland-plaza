from rest_framework import serializers

from .models import *


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        exclude = ["modified_at"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        models = Comments
        exclude = ["modified_at"]
